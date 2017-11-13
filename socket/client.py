import socket, sys

UDP_IP = "178.48.49.12"    # pc
#UDP_IP =  "37.76.56.237"
UDP_PORT = 5005
MESSAGE = b"Helllo, World!"

if (len(sys.argv) >= 2):
    MESSAGE = sys.argv[1].encode('ascii')

print("UDP target IP:" + UDP_IP)
print("UDP target port:" + str(UDP_PORT))
print("message:" + MESSAGE.decode('ascii'))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet, UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))    # takes bytes string