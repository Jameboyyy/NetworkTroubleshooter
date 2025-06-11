# src/main.py

from ping import check_device
from traceroute import traceroute_to_device
from utils import log_to_file, send_alert
import config
import datetime
import requests

def main():
    issues_found = False
    report = []
    now = datetime.datetime.now().strftime('%Y-%m-%d %I:%M %p')
    report.append(f"📡 Network Status Report — {now}\n")

    # Check router
    ok, status = check_device("Router", config.ROUTER_IP)
    report.append(status)
    if not ok:
        issues_found = True

    # Check external IP (internet)
    ok, status = check_device("Internet", config.EXTERNAL_IP)
    report.append(status)
    if not ok:
        issues_found = True

    # Check additional devices
    if "DEVICES" in config.config:
        for name, device_ip in config.config["DEVICES"].items():
            ok, status = check_device(name, device_ip)
            report.append(status)
            if not ok:
                issues_found = True

    # Try public IP
    try:
        public_ip = requests.get("https://api.ipify.org", timeout=5).text
        report.append(f"\n🌐 Public IP: {public_ip}")
    except:
        report.append("\n🌐 Public IP: ❌ Failed to fetch")
        issues_found = True

    # Traceroute (optional)
    try:
        traceroute_lines = traceroute_to_device(config.EXTERNAL_IP)
        report.append("\nTraceroute:")
        report.extend(traceroute_lines)
    except Exception as e:
        report.append(f"❌ Traceroute failed: {e}")
        issues_found = True

    final_report = "\n".join(report)

    # Always log
    log_to_file(final_report)

    # Only email if something went wrong
    if issues_found:
        try:
            send_alert("🚨 Network Issue Detected", final_report)
        except Exception as e:
            log_to_file(f"❌ Failed to send alert: {e}")

    # Print for manual check
    print(final_report)

if __name__ == "__main__":
    main()
