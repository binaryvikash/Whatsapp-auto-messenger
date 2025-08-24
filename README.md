# WhatsApp Automation Bot

A Python-based WhatsApp automation bot that allows you to send messages to multiple contacts automatically. It uses **Selenium** and **undetected-chromedriver** to interact with WhatsApp Web. Schedule messages via YAML files and manage contacts via CSV. Perfect for reminders, notifications, or bulk messaging.

---

## Features

- Send WhatsApp messages automatically via WhatsApp Web.  
- Schedule messages with flexible timing using YAML files.  
- Manage multiple recipients via CSV files.  
- Supports plain text messages (emoji support may vary depending on ChromeDriver).  
- Logging of sent messages and errors.  

---

## Use Cases

- Sending reminders or notifications.  
- Bulk messaging for personal or small business use.  
- Scheduled greetings, announcements, or alerts.  

---

## Requirements

- Python 3.9+  
- Chrome or Chromium browser  
- ChromeDriver compatible with your browser version  
- Python packages:
  - `selenium`
  - `undetected-chromedriver`
  - `pandas`
  - `pyyaml`
  - `apscheduler`  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

## Install

```bash
Linux / Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate


pip install -r requirements.txt
