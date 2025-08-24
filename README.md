# Whatsapp-auto-messenger
A Python-based WhatsApp automation bot that allows you to send messages to multiple contacts automatically. Uses Selenium and undetected-chromedriver to interact with WhatsApp Web. Schedule messages via YAML files and manage contacts via CSV. Perfect for reminders, notifications, or bulk messaging


WhatsApp Automation Bot

Automate sending WhatsApp messages to multiple contacts on a schedule using Python and Selenium. Supports CSV-based contact lists and YAML-based message scheduling.

Features :

Send WhatsApp messages automatically via WhatsApp Web.
Schedule messages with flexible timing using YAML files.
Manage multiple recipients via CSV files.
Supports plain text messages (emojis support may vary depending on ChromeDriver).
Logging of sent messages and errors.

Use Cases :

Sending reminders or notifications.
Bulk messaging for personal or small business use.
Scheduled greetings, announcements, or alerts.

Requirements :

Python 3.9+
Chrome or Chromium browser
ChromeDriver compatible with your browser version
pip packages
selenium
undetected-chromedriver
pandas
pyyaml
apscheduler

Installation

Clone the repository:
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
Create a virtual environment (optional but recommended):
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

Install dependencies :

pip install -r requirements.txt
Make sure chromedriver is available and matches your Chrome version.
Configuration
Recipients CSV

Create a CSV file at config/recipients.csv with the following format:

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


Time should be in 24-hour HH:MM format.

Usage

First time: Run the bot manually to scan the WhatsApp QR code:

python3 send_message.py



Notes

Ensure your browser and ChromeDriver versions are compatible.

WhatsApp Web must be logged in via QR code scanning initially.

Emoji support may be limited depending on ChromeDriver.
