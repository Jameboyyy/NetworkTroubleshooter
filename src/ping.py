from ping3 import ping

def check_device(name, device_ip):
    response = ping(device_ip, timeout=2)
    if response:
        return True, f"✅ {name} ({device_ip}) is reachable ({round(response * 1000, 1)} ms)"
    else:
        return False, f"❌ {name} ({device_ip}) is unreachable"
