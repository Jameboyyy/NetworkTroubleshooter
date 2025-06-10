# src/main.py

from ping import check_device
from traceroute import traceroute_to_device
from utils import log_to_file, send_alert
import config

def main():

    # Pings the Router
    check_device(config.ROUTER_IP)

    # Perform a traceroute to an external IP
    traceroute_to_device(config.ExternalIP)

    # Log the results
    log_to_file("Network check completed.")

    # send an alert if something goes wrong
    send_alert("Network issue detected.")

    if __name__ == "__main__":
        main()