import binascii, socket, sys
from datetime import datetime

def hex_encode(_input):
    _input = str(_input).encode('ascii')
    bytess = binascii.hexlify(_input)        
    return bytess.decode('ascii')

#UDP_IP = "152.66.130.2"    # sunos
UDP_IP = "178.48.49.12"    # pc
#UDP_IP =  "37.76.56.237"
UDP_PORT = 5005
MESSAGE = b"Helllo, World!"

if (len(sys.argv) >= 2):
    MESSAGE = hex_encode(sys.argv[1])
    MESSAGE = MESSAGE.encode('ascii')   # not needed for sending over NB-IoT

print("Sent message at " + datetime.now().strftime("%H:%M:%S.%f"))
print("message: " + sys.argv[1])
print("encoded: " + MESSAGE.decode('ascii'))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))    # takes bytes string