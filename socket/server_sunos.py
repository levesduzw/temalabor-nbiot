import socket, binascii
from datetime import datetime

def hex_decode(_input):   # float -> string
    bytess = binascii.unhexlify(_input)
    return bytess.decode('ascii')

UDP_IP = "152.66.130.2"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print data
    print type(data)
    print(datetime.now().strftime("%H:%M:%S"), "Received message:", hex_decode(data))
    sock.sendto(b'ok', addr)