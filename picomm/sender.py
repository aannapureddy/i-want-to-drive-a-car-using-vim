import socket
 
UDP_IP = "10.20.5.121"
UDP_PORT = 6970
MESSAGE = "Hello, World!".encode()

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", 'MESSAGE'.encode('utf-8'))

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
