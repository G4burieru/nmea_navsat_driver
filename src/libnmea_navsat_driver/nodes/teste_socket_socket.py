import socket
from time import sleep

while 1:
    msg = b'hello world'
    # print(f'sending on {ip}')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    # sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.setsockopt(socket.SOL_SOCKET, 25, str("vr-br" + '\0').encode('utf-8'))
    sock.bind(("192.168.0.100",7777))
    sock.sendto(msg, ("192.168.1.255", 6666))
    # sock.close()
