import binascii, socket, sys

def hex_encode(_input):   # float -> string
    _input = str(_input).encode('ascii')
    bytess = binascii.hexlify(_input)        
    return bytess.decode('ascii')

UDP_IP = "152.66.130.2"    # sunos
UDP_PORT = 5005
MESSAGE = b"Helllo, World!"

if (len(sys.argv) >= 2):
    MESSAGE = hex_encode(sys.argv[1])
    MESSAGE = MESSAGE.encode('ascii')   # not needed for sending over NB-IoT

print("UDP target IP:" + UDP_IP)
print("UDP target port:" + str(UDP_PORT))
print("message:" + sys.argv[1] + " encoded: " + str(MESSAGE))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet, UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))    # takes bytes string