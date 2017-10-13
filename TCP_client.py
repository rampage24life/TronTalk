import socket
import sys

HOST, PORT = "localhost", 9999
data = input("Message: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT)) #Open connection to socket
    sock.sendall(bytes(data + "\n", "utf-8")) #Send bytes to TCP

print("Sent:     {}".format(data))