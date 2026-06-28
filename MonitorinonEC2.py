#!/usr/bin/env python3

import os
import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Configs
LOG_FILE="/var/log/auth.log"
SENDER_EMAIL=os.getenv("SENDER_EMAIL")
SENDER_PASSWORD=os.getenv("SENDER_PASSWORD")
RECEIVER_EMAIL="Hariomharish50@gmail.com"

msg=MIMEText("This is an Testing Email for SSH MONITORING")
msg["Subject"]="Test Email - SSH MONITOR SETUP"
msg["From"]=SENDER_EMAIL
msg["To"]=RECEIVER_EMAIL


try:
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
        server.login(SENDER_EMAIL,SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL,RECEIVER_EMAIL,msg.as_string())
        print("[OK] Test Email Working..")
except Exception as e:
    print(f"[Error] Email Failed : {e}")

