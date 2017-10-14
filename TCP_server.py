import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler, socketserver.ThreadingMixIn):
  """
    The request handler class for the server.
  """

  def handle(self):
    """
    Handle Function
    This function must do all the work required to service a request. 
    The default implementation does nothing.
    """
    self.data = self.request.recv(1024).strip()
    """
    The type of self.request is different for datagram or stream services.
    For stream, self.request is a socket object.
    For datagram, self.request is a pair of string and socket.
    """
    print("Hello ", self.data.decode()) #print data
    self.request.sendall(self.data.upper())

if __name__ == "__main__":
    #HOST, PORT = "localhost", 9999
    HOST = input("Host (default=localhost): ") or "localhost"  # Input host
    PORT = input("Port (default=9999): ") or 9999 # Input port
    PORT = int(PORT)
    
    print("Server: "+HOST+":"+str(PORT))

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server: #Run server
        server.serve_forever() 
