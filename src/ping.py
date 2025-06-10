from ping3 import ping

def check_device(device_ip):
    response = ping(device_ip)
    if response: 
        print(f"{device_ip} is reachable with {response} ms latency")
    else: 
        print(f"{device_ip} is unreachable")