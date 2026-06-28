import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(sender_email, sender_password, receiver_email, subject, body):
    # Create email message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] =".".join(receiver_email)
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        # Connect to Gmail SMTP Server                  
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()   # Enable TLS
        server.login(sender_email, sender_password)

        server.sendmail(sender_email, receiver_email,msg.as_string()
        )

        server.quit()
        print("✅ Email Sent Successfully!")

    except Exception as e:
        print("❌ Error:", e)


# Function Call
send_email(
    sender_email="hariomharish50@gmail.com",
    sender_password="rdsn reml rjet vtnv",
    receiver_email=["arvind12974@gmail.com","chalhatpatanhi@gmail.com","sudhirkushwaha10@gmail.com"],
    subject="Testing Email Sender Using Pure Python",
    body="Hello! This email is sent from Python programming."
)