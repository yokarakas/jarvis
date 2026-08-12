"""
actions/osint_lookup.py — Username OSINT sweep via Sherlock (sherlock-project).

Searches a given username across hundreds of social platforms and reports
which ones have a matching public profile. Streams results live as they're
found — a full sweep checks 400+ sites and can take 1–3 minutes depending
on your network, so this reports progress instead of going silent.

Legitimate use only: checking your own digital footprint, username
availability, or security research with the account holder's consent.
Do not use this to locate, monitor, or harass a real person without
their permission.

Install:  pip install sherlock-project
"""
from __future__ import annotations

import platform
import re
import shutil
import subprocess
import sys
import time

_OS = platform.system()
_WIN_HIDE = {"creationflags": subprocess.CREATE_NO_WINDOW} if _OS == "Windows" else {}

_FOUND_RE     = re.compile(r"^\[\+\]\s*([^:]+):\s*(\S+)\s*$")
_MAX_LISTED   = 40
_HARD_TIMEOUT = 240   # seconds — hard cap, process is killed past this
_PING_EVERY   = 20    # seconds — "still running" heartbeat to the log


def _sherlock_cmd() -> list[str]:
    """Prefer the installed console script; fall back to the module entrypoint."""
    if shutil.which("sherlock"):
        return ["sherlock"]
    return [sys.executable, "-m", "sherlock_project"]


def osint_lookup(parameters: dict, response=None, player=None) -> str:
    username = (parameters.get("username") or "").strip()
    if not username:
        return "No username was provided for the OSINT lookup."

    # basic sanity guard — sherlock takes a bare username, not a URL/handle with spaces
    username = username.lstrip("@").strip()
    if not username or " " in username:
        return "Please provide a single valid username (no spaces, no @ or URL)."

    if player:
        player.write_log(f"SYS: OSINT sweep started for '{username}' — this can take 1-3 minutes.")

    cmd = _sherlock_cmd() + [username, "--print-found", "--no-color", "--timeout", "5"]

    try:
        proc = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
            text=True, bufsize=1, **_WIN_HIDE
        )
    except FileNotFoundError:
        msg = "Sherlock is not installed. Run: pip install sherlock-project"
        if player:
            player.write_log(f"ERR: {msg}")
        return msg
    except Exception as e:
        return f"OSINT sweep failed to start: {e}"

    found: list[tuple[str, str]] = []
    start, last_ping = time.monotonic(), time.monotonic()
    timed_out = False

    try:
        for line in proc.stdout:
            m = _FOUND_RE.match(line.strip())
            if m:
                site, url = m.group(1).strip(), m.group(2).strip()
                found.append((site, url))
                if player:
                    player.write_log(f"OSINT: {site} — {url}")

            now = time.monotonic()
            if now - start > _HARD_TIMEOUT:
                timed_out = True
                proc.kill()
                break
            if now - last_ping > _PING_EVERY:
                if player:
                    player.write_log(
                        f"SYS: OSINT sweep still running… "
                        f"({int(now - start)}s elapsed, {len(found)} found so far)"
                    )
                last_ping = now
    finally:
        try:
            proc.wait(timeout=5)
        except Exception:
            proc.kill()

    if timed_out:
        if player:
            player.write_log(f"SYS: OSINT sweep for '{username}' stopped at the time limit.")
        if found:
            lines = [f"{site}: {url}" for site, url in found[:_MAX_LISTED]]
            return (
                f"OSINT sweep for '{username}' hit the time limit but found "
                f"{len(found)} profile(s) before stopping:\n" + "\n".join(lines)
            )
        return f"OSINT sweep for '{username}' hit the time limit before finding anything."

    if not found:
        if player:
            player.write_log(f"SYS: OSINT sweep — no public profiles found for '{username}'.")
        return f"No public profiles were found for the username '{username}'."

    if player:
        player.write_log(f"SYS: OSINT sweep finished — {len(found)} profile(s) found for '{username}'.")

    lines   = [f"{site}: {url}" for site, url in found[:_MAX_LISTED]]
    summary = (
        f"Found {len(found)} public profile(s) for username '{username}':\n"
        + "\n".join(lines)
    )
    if len(found) > _MAX_LISTED:
        summary += f"\n…and {len(found) - _MAX_LISTED} more (see the activity log)."
    return summary
