from requirements.library import *


def Socket(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host,port))
    server.listen()
    return server
  
  
class Server:
    def __init__(self, host='127.0.0.1', port=1234):
        self.server = Socket(host, port)
        self.client = []


    def Accept(self,*args):
        while True:
             available_socket, _, disconnected_socket = select.select(self.client, [], self.client) 

             for client in available_socket:
                  if client == self.server:
                      client_socket, address = client.accept()
                      self.client.append(client_socket)
                      Message = b'Welcome'
                      self.Send(client_socket, Message) 

                  else:
                      Message = self.Receive(client)
                      if len(Message)!=0:
                          self.Send(client, Message)
                      
             for client in disconnect_socket:
                  del client
                  self.client.remove(client)
                  
                  
    def Receive(self, client):
        message=b''
        try:
          while True:
              msg = client.recv(20)
              if len(message)==0:
                  return message
                  
              message+=msg
        except:
            pass
          
          
    def Send(self, client, message):
        for client_socket in self.client:
            if client_socket != client:
                client_socket.send(message)
              
 
