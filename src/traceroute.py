from scapy.all import traceroute

def traceroute_to_device(device_ip):
    try:
        result, unanswered = traceroute(device_ip, verbose=False)
        return [f"{snd.src} ➝ {rcv.dst} - {rcv.time - snd.time:.2f}s"
                for snd, rcv in result]
    except Exception as e:
        return [f"❌ Traceroute failed: {e}"]
