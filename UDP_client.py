import socket
import sys

#UDP_IP = "127.0.0.1"
#UDP_PORT = 5555
#MESSAGE = input("Message: ").encode()

#HOST, PORT = "localhost", 9999
#data = input("Message: ")

HOST = input("Host (default=localhost): ") or "localhost"  # Input host
PORT = input("Port (default=9999): ") or 9999 # Input port
PORT = int(PORT)
data = input("Message: ") # Input message

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Create socket connection

#sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT)) #Send bytes to UDP
received = str(sock.recv(1024), "utf-8")

print("Sent:     {}".format(data))
