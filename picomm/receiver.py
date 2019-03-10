import socket
from command import decode
UDP_IP = "10.20.5.121"
UDP_PORT = 6970
 
sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    throttle, steering = decode(data)
    print('Throttle', throttle)
    print('Steering', steering)