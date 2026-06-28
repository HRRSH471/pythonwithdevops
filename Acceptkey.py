    #!/usr/bin/env python3

import os
import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configurations
LOG_FILE = "/var/log/auth.log"
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECEIVER_EMAIL = "hariomharish50@gmail.com"


def build_email_body(username, ip_address, method, timestamp):
    return f"""
SSH Login Alert

User      : {username}
From IP   : {ip_address}
Method    : {method}
Time      : {timestamp}
"""


def send_email(username, ip_address, method, timestamp):
    subject = f"SSH Login Alert: {username} logged in"

    body = build_email_body(username, ip_address, method, timestamp)

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(
                SENDER_EMAIL,
                RECEIVER_EMAIL,
                msg.as_string()
            )
            print(f"[OK] Mail sent for {username} - {ip_address} to {RECEIVER_EMAIL}")

    except Exception as e:
        print(f"[ERROR] Email failed: {e}")


def check_log_for_login(line):
    if "Accepted" not in line:
        return

    words = line.split()

    try:
        accepted_index = words.index("Accepted")

        method = words[accepted_index + 1]
        username = words[accepted_index + 3]
        ip_address = words[accepted_index + 5]

    except Exception:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    send_email(username, ip_address, method, timestamp)


def watch_log():
    print(f"[INFO] watching {LOG_FILE} for SSH Logins...")
    with open(LOG_FILE, "r") as f:

        # Move to the end of the file
        f.seek(0, 2)

        while True:
            line = f.readline()

            if not line:
                time.sleep(1)
                continue

            check_log_for_login(line)


if __name__ == "__main__":
    watch_log()