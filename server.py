from Requirements.library import *
  
class Server:
    def __init__(self, host='127.0.0.1', port=1234):
        self.server = self.Socket(host, port)
        self.client = [self.server]

    def Socket(self,host, port):
	    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	    server.bind((host,port))
	    server.listen()
	    return server

    def Accept(self,*args):
        while True:
             available_socket, _, disconnected_socket = select.select(self.client, [], self.client) 

             for client in available_socket:
                  if client == self.server:
                      client_socket, address = client.accept()
                      self.client.append(client_socket)
                      print(f'successfully connected with {address[0]}')
                      Message = b'Welcome'
                      client_socket.send(Message)

                  else:
                      Message = self.Receive(client)
                      if len(Message)!=0:
                          self.Send(client, Message)
                      
             for client in disconnected_socket:
                  client.close()
                  self.client.remove(client)
                  
                  
    def Receive(self, client):
        try:
          while True:
              msg = client.recv(1024)
              if len(msg)!=0:
                  return msg
                    
        except:
            pass
          
          
    def Send(self, client, message):
        for i in self.client[1:]:
            if i!=client:
                i.send(message)

                
if __name__ == '__main__':
	app = Server()
	app.Accept()
              
 
