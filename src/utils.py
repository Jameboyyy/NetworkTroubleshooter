import logging
import smtplib
from email.message import EmailMessage
from config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECIPIENT

def log_to_file(message):
    logging.basicConfig(filename='network_troubleshooter.log', level=logging.INFO)
    logging.info(message)

def send_alert(subject, message):
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECIPIENT

    try: 
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("Alert email sent")
    except Exception as e:
        print(f"Failed to send alert: {e}")