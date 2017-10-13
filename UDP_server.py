"""
    Goal is to create a server applicatoin that listens on a UDP network
    and when it receives a string, it will respond "Hello <string>"
"""

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
    """
        The request handler class for the server.
    """

    def handle(self):
        """
        Handle funciton:
        This function must do all the work required to service a request.
        The default implementation does nothing.
        Several instance attributes are avaliable to it:
            the request is available as "self.request"
            the client address as "self.client_address"
            the server instance as "self.server" (in case it needs access to
                per-server information.
        """
        #get data
        data = self.request[0].strip()
        
        socket = self.request[1]
        print("Hello ", data.decode())
        socket.sendto(data.upper(), self.client_address)


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    print("Server: " + HOST + ":" + str(PORT))
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        server.serve_forever()
#Server stop when you click Ctrl-D
