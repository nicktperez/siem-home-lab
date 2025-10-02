#!/usr/bin/env python3
import socket, time, random

HOST = "127.0.0.1"  # Logstash is exposed on your Mac via Docker
PORT = 5514         # UDP syslog port we mapped

messages = [
    "Failed password for invalid user root from 10.0.0.5 port 34567 ssh2",
    "Failed password for invalid user admin from 10.0.0.5 port 34568 ssh2",
    "Failed password for user nick from 192.168.56.23 port 50122 ssh2",
    "Failed password for user test from 203.0.113.77 port 55110 ssh2",
    "Failed password for invalid user ubuntu from 10.10.10.10 port 44444 ssh2",
]

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for _ in range(250):
    msg = random.choice(messages)
    # prepend a simple syslog-ish header; Logstash doesn’t require strict RFC here
    payload = f"<14> host sshd: {msg}"
    sock.sendto(payload.encode(), (HOST, PORT))
    time.sleep(0.03)

print("Done sending demo syslog messages.")