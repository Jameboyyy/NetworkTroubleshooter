import json

def load_config():
    with open('config.json') as config_file:
        config_data = json.load(config_file)
    return config_data

config = load_config()
ROUTER_IP = config['ROUTER_IP']
EXTERNAL_IP = config['EXTERNAL_IP']

print(f"Router IP: {ROUTER_IP}")
print(f"EXTERNAL IP: {EXTERNAL_IP}")

