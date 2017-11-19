import socket, binascii
from datetime import datetime

def hex_decode(_input):   # float -> string
    bytess = binascii.unhexlify(_input)
    return bytess.decode('ascii')

UDP_IP = "192.168.0.16"   # ipconfig IPv4 address 
#UDP_IP = "100.75.10.174"  # mobile data
#UDP_IP = "192.168.0.19"   # wlan0
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet, UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes   class 'bytes'
    print("Received message at", datetime.now().strftime("%H:%M:%S.%f"))  # hex_decode(data))   # for NBIoT packets - message format??
    print("encoded: " + data.decode('ascii'))
    print("message: " + hex_decode(data) + '\n')
    sock.sendto(b'ok', addr)