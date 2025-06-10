from scapy.all import traceroute

def traceroute_to_device(device_ip):
    result, unanswered = traceroute(device_ip)
    result.show()