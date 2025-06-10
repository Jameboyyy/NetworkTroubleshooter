import logging

def log_to_file(message):
    logging.basicConfig(filename='network_troubleshooter.log', level=logging.INFO)
    logging.info(message)

def send_alert(message):
    print(f"Alert: {message}")