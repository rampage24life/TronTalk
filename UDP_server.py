#import socket
import socketserver


# UDP_IP = "127.0.0.1"
# UDP_PORT = 5555
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.bind((UDP_IP, UDP_PORT))

# print("UDP SERVER: "+UDP_IP+":"+str(UDP_PORT))

# while True:
#     data, addr = sock.recvfrom(1024)
#     print("Hello "+data.decode())

class MyUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print("Hello ", data.decode())
        socket.sendto(data.upper(), self.client_address)


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    print("Server: " + HOST + ":" + str(PORT))
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        server.serve_forever()
