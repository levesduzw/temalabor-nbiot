import socket, binascii
from datetime import datetime

def hex_decode():   # hex string -> string
    bytess = binascii.unhexlify(_input) # returns Python 'bytes'
    return bytess.decode('ascii')   # returns Python 'str'

UDP_IP = "152.66.130.2"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print("Received message at " + datetime.now().strftime("%H:%M:%S.%f"))
    data = data.strip()
    print(data + '#')
    print(type(data))   # 'str', not 'bytes'
    print("encoded: " + data.decode('ascii'))
    #print("message: " + hex_decode(data) + '\n')   # not needed!

    with open("data.txt", 'w') as file:
        file.write(data.decode('ascii'))