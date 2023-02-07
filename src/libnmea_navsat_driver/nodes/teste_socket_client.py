import socket
import time

IP = '192.168.0.100'  # IP address of the desired interface
PORT = 6666

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, 25, str("vr-br" + '\0').encode('utf-8'))
# s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((IP, PORT))

# s.recvfrom(1024)
while 1:
    data, addr = s.recvfrom(1024)
    print("received message:", data, "from", addr)
    time.sleep(2)
