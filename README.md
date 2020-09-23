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
There are two major task of server:
* Accept new incoming connection
* Accept incoming data from active client and forward it to other client

Task of client is to:  
- Read/send data from/to server
<br />

#### Process Flow Chart
<br />
<br />
<br />
<p align="center"><img  src="https://github.com/PankajKumar2609/SocketTutorial/blob/patch1/Gallery/ProcessChart.png?raw=true"></p>
<br />
<br />
<br />

#### Protocols
- **TCP** - socket.SOCK_STREAM  
- **UDP** - socket.SOCK_DGRAM    
- **IPv4** - socket.AF_INET  
- **IPv6** - socket.AF_INET6  
