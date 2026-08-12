> ⚠️ **This project is currently under active development.** If you'd like to contribute, share suggestions, or collaborate, feel free to reach out via Instagram: [**@yokarakas**](https://www.instagram.com/yokarakas)

# ⚙️ MARK LS — JARVIS
### The Ultimate Cross-Platform Personal AI Assistant — By karakas

A real-time voice AI that can hear, see, understand, and control your computer — on any OS. Supports Windows, macOS, and Linux. Built on the Gemini Live API for native audio streaming, delivering zero subscriptions and total digital autonomy.

---

## ✨ Overview

MARK LS is where the assistant stops being a tool and starts being a presence. It remembers yesterday's conversation, watches the topics you care about, and speaks first when it has something worth saying. The goal of this build was continuity — JARVIS should feel like it never fully left, even after you close it.

It's not just an assistant — it's an extension of your digital life.

---

## 🚀 Complete Capabilities & Features

### 🎙️ Core & Voice Capabilities
| Feature | Description |
|---|---|
| **Real-time Voice** | Ultra-low latency bidirectional audio conversation in any language via Gemini Live API |
| **Silent Language Memory** | Automatically detects spoken language on first use and adapts all future sessions seamlessly |
| **Hybrid Input** | Effortlessly switch between keyboard typing and voice interaction on demand |
| **Assistant Customization** | Dynamically change assistant and user names from the UI with immediate effect |
| **Auto-Start on Boot** | Configures native system startup services (Windows Registry, macOS LaunchAgent, Linux systemd/desktop) |

### 🕵️ Intelligence & OSINT
| Feature | Description |
|---|---|
| **Sherlock OSINT Search** | Fast username footprint lookup across **400+ social media platforms** and websites |
| **Multi-Mode Web Search** | Dynamic `news` / `research` / `price` / `compare` / `search` modes via Gemini Grounded search with DuckDuckGo fallback |
| **Clipboard Intelligence** | Automatic text capture floating HUD offering instant Translate, Summarize, Explain, or Code Fix actions |
| **Flight Finder** | Direct querying for real-time flight options, prices, and route availability |

### 📱 Device Control & System Automation
| Feature | Description |
|---|---|
| **Remote Mobile Dashboard** | Full phone control, screen access, and remote trigger execution paired securely via QR code |
| **OS System Control** | Launch applications, adjust system volume and brightness, manage WiFi, execute power commands, and trigger global shortcuts |
| **Desktop & Window Management** | Direct manipulation of OS taskbars, active window focuses, and desktop workspace operations |
| **Browser Integration** | Open URLs, manage active tabs, and navigate websites hands-free via voice commands |
| **Messaging Integration** | Compose and deliver messages through integrated services like WhatsApp and Telegram |
| **YouTube Media Controls** | Search media, trigger video playback, and adjust playback parameters via natural language |
| **Autonomous Task Agent** | High-level goal planning and execution for complex, multi-step actions |

### 👁️ Vision & Hardware Monitoring
| Feature | Description |
|---|---|
| **Visual Awareness** | Real-time desktop screen streaming and webcam video feeds piped directly into active Gemini sessions |
| **Hardware Telemetry** | Continuous real-time monitoring of CPU, RAM, GPU, and temperature metrics with localized voice warnings |
| **Dynamic Content Panel** | Scrollable UI layer under the main HUD displaying web pages, news previews, and search data |

### 🧠 Persistent Context & Memory System
| Feature | Description |
|---|---|
| **Persistent Memory** | Long-term memory store tracking projects, preferences, and multi-session contextual data |
| **Morning Briefing** | Boot sequence routine: greets the user, announces time, recaps previous context, and pulls live daily news |
| **Proactive 2.0 Check-ins** | Contextual proactive prompts based on time of day, active projects, and past conversation threads |
| **Session Memory** | Auto-summarizes ended sessions and references relevant context the following morning before expiring safely |
| **Background Topic Monitor** | User-defined daily background monitoring for specific news or topic headlines |
| **Weather Integration** | Real-time city weather updates tailored using stored location memory |

### 💻 Developer & Utility Tools
| Feature | Description |
|---|---|
| **Code Helper Agent** | Inline code review, debugging assistance, refactoring, and code generation |
| **File Processing** | Direct file inspection, content summarization, and query execution against local document files |
| **Smart OS Reminders** | System-native scheduled notifications leveraging native schedulers (Task Scheduler / LaunchAgent / systemd) |
| **Game Updater** | On-demand status checks and update triggers for Steam and Epic Games libraries |

---

## ⚡ Quick Start

git clone https://github.com/yokarakas/jarvis.git
cd Mark-LS
pip install -r requirements.txt
python main.py