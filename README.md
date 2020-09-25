## Socket!
*A socket is one endpoint of a two-way communication link between two programs running on the network.*

              
<br />
<br />
<br />
<p align="center"><img  src="https://github.com/PankajKumar2609/SocketTutorial/blob/patch1/Gallery/SocketBasic.png?raw=true"></p>
<br />
<br />
<br />



***Program1 and Program2 are client which communicating with each other and Endpoint is server which actively listening at particular IP address & port.***<br />
<br />
*There are two major task of server:*
* *Accept new incoming connection*
* *Accept incoming data from active client and forward it to other client*

*Task of client is to:*  
- *Read/ send data from/ to server*
<br />

#### *Process Flow Chart*
<br />

<p align="center"><img  src="https://github.com/PankajKumar2609/SocketTutorial/blob/patch1/Gallery/ProcessChart.png?raw=true"></p>

<br />
<br />
<br />


#### *Server Main Parts*
- ***Initialise** - Creating socket object.*<br />
                 *server = socket.socket(socket.SOCK_STREAM, socket.AF_INET)*
                 <br />
                 
- ***Bind** - Bind initialised socket to IP and port.*<br /> 
            *server.bind(('127.0.0.1',1234)) #binding to local host at port 1234 or use your network IPv4 address to which server is connected.*
                <br />
                
- ***Listen** - Start listening to incoming request at bind address and port.*<br />
*server.listen()*

- ***Accept** - Accept new connections if any request comes at above address.*<br />
*rclient, address = server.accept()*<br />
***rclient** is socket object of received connection and will further used to receive/ send data.*<br />
***address** contains IP address & port number of new connection.*
<br />


#### *Client Main Parts*
- ***Initialse** - Creating socket object.*<br />
                 *client = socket.socket(socket.SOCK_STREAM, socket.AF_INET)* 

- ***Connect** - To Connect with the server provide same address & port number at which server is listening.*<br />
*client.connect(('127.0.0.1',1234))*<br />
<br />


#### *Send/Receive Data*
- ***send()** is used to forward data from client/ server to server/client.*<br />
*client.send(data)/ server.send(data)*<br />
*Sockets transmit streams of bytes, so don't forget to encode your data into byte.*<br />
*data.encode('utf-8')*

- ***recv()** is used to receive data from client/ server.*<br />
*client.recv(24)/ server.recv(1024)*<br />
*Here, 1024 is size which means at a time it can only read atmost 1024 bytes.*
<br />


#### *Network Protocols*
- **TCP** - *socket.SOCK_STREAM* 
- **UDP** - *socket.SOCK_DGRAM*    

#### *Address Family*
- **IPv4** - *socket.AF_INET*  
- **IPv6** - *socket.AF_INET6*  

#### *Select*
select.select returns three separate list containing writable, readable and disconnected/ inactive socket from a given list.
