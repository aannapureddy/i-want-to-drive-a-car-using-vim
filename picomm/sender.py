import socket
from command import encode
UDP_IP = "10.20.5.121"
UDP_PORT = 6970
MESSAGE = "Hello, World!".encode()



def send(throttle, steering, verbose=False):

    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    MESSAGE = encode(throttle, steering)
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))    
    if verbose:
        print("UDP target IP:", UDP_IP)
        print("UDP target port:", UDP_PORT)
        print("message:", 'MESSAGE'.encode('utf-8'))


send(10, 20)
send(-120, 120)
send(100, -119, True)