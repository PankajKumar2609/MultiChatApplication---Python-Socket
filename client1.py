from Requirements.library import *
  
class Client:
    def __init__(self, host='127.0.0.1', port=1234):
        self.client = self.Socket(host, port)
        message = threading.Thread(target = self.Message)
        receive = threading.Thread(target = self.Receive)
        message.start()
        receive.start()

    def Socket(self,host, port):
	    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    client.connect((host,port))
	    return client

    def Receive(self, *args):
        try:
          while True:
              msg = self.client.recv(1024)
              if len(msg)!=0:
                  print(msg)
                    
        except:
            pass
          
          
    def Message(self, *args):
        while True:
            msg='client1-'
            msg += input()
            msg = msg.encode('utf-8')
			
            self.client.send(msg)

if __name__ == '__main__':
	app = Client()
