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

```bash
# 1. Clone the repository and navigate into it
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# 2. Create a virtual environment (optional but recommended) and activate it
# Linux / Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Set up ChromeDriver
# Make sure ChromeDriver is available and matches your Chrome/Chromium version.
# Place it in a path accessible by the bot, or update `send_message.py` with the correct path.


## Configuration

### Recipients CSV

Create a CSV file at `config/recipients.csv` with the following format:

```csv
number,name
918123456789,John
917987654321,Alice


Schedule YAML

Create a YAML file at config/schedule.yml:

messages:
  - text: "Hello! This is a scheduled message."
    time: "10:00"
  - text: "Don't forget the meeting at 3 PM."
    time: "14:30"


Note: Time should be in 24-hour HH:MM format.


## Usage

### 1. Run the bot manually (first time)

Scan the QR code in WhatsApp Web:

```bash
python3 send_message.py


