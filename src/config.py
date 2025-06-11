import json
import os

# Get the full path to config.json in the parent directory
config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')

with open(config_path) as config_file:
    config_data = json.load(config_file)

ROUTER_IP = config_data['ROUTER_IP']
EXTERNAL_IP = config_data['EXTERNAL_IP']
EMAIL_SENDER = config_data['EMAIL']['SENDER']
EMAIL_PASSWORD = config_data['EMAIL']['APP_PASSWORD']
EMAIL_RECIPIENT = config_data['EMAIL']['RECIPIENT']

config = config_data

print(f"Router IP: {ROUTER_IP}")
print(f"EXTERNAL IP: {EXTERNAL_IP}")


