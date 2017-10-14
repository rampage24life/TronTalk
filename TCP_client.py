import socket
import sys

#HOST, PORT = "localhost", 9999
HOST = input("Host (default=localhost): ") or "localhost"  # Input host
PORT = input("Port (default=9999): ") or 9999 # Input port
PORT = int(PORT)
data = input("Message: ") #Input message

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT)) #Open connection to socket
    sock.sendall(bytes(data + "\n", "utf-8")) #Send bytes to TCP

print("Sent:     {}".format(data))
