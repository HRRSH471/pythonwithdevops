import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage


def send_email(sender_email, sender_password, receiver_email, subject, body, files):
        # Create email message
        msg = EmailMessage()
        msg["From"] = sender_email
        msg["To"] =",".join(receiver_email)
        msg["Subject"] = subject

        msg.set_content(body)

        for file_path in files:
            try:                
                with open(file_path,"rb") as attach:
                    msg.add_attachment(
                    attach.read(),
                    maintype="application",
                    subtype="octet-stream",
                    filename=file_path.split("/")[-1] 
            )

            except Exception as e:
                print("❌ Error:", e)
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
        files=["greet.txt"],
        sender_email="hariomharish50@gmail.com",
        sender_password="rdsn reml rjet vtnv",
        receiver_email=["Hariomharish50@gmail.com","sudhirkushwaha10@gmail.com"],
        subject="Testing Email Sender Using Pure Python",
        body="Hello! This email is sent from Python programming."
    )