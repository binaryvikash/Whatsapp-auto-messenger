import time
import logging
import pandas as pd
import yaml
from apscheduler.schedulers.blocking import BlockingScheduler
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup logging
logging.basicConfig(filename="automation.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Load recipients from CSV
def load_recipients(file="config/recipients.csv"):
    return pd.read_csv(file)

# Load schedule from YAML
def load_schedule(file="config/schedule.yml"):
    with open(file, "r") as f:
        return yaml.safe_load(f)

# Setup browser
def setup_browser():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-notifications")
    options.add_argument("--start-maximized")

    driver = uc.Chrome(
        options=options,
        browser_executable_path="/usr/bin/chromium-browser",  # chromium
        driver_executable_path="/home/vikash/chromedriver"   # your copy
    )

    driver.get("https://web.whatsapp.com")
    print("Waiting for QR scan...")

    # ✅ Wait until the sidebar loads (means QR login done)
    WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.XPATH, '//div[@id="pane-side"]'))
    )

    print("Login successful!")
    return driver

# Send message
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def send_message(driver, number, message):
    try:
        # Open chat URL
        driver.get(f"https://web.whatsapp.com/send?phone={number}")
        
        # Wait until chat header is visible (chat loaded)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//header//span[@title]'))
        )

        # Then locate the message input inside the chat footer
        input_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((
                By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'
            ))
        )

        input_box.click()
        time.sleep(1)
        input_box.send_keys(message)
        input_box.send_keys(Keys.ENTER)

        logging.info(f"Message sent to {number}")
        time.sleep(2)

    except Exception as e:
        logging.error(f"Failed to send to {number}: {e}")

# Job execution
def job(driver, recipients, message):
    for _, row in recipients.iterrows():
        send_message(driver, row["number"], message)

def main():
    recipients = load_recipients()
    schedule = load_schedule()
    driver = setup_browser()

    scheduler = BlockingScheduler()

    for item in schedule["messages"]:
        msg_text = item["text"]
        run_time = item["time"]  # "HH:MM" format
        hour, minute = map(int, run_time.split(":"))

        scheduler.add_job(job, "cron", [driver, recipients, msg_text],
                          hour=hour, minute=minute)

    logging.info("Scheduler started...")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        driver.quit()

if __name__ == "__main__":
    main()

