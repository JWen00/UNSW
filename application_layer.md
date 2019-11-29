# Appplication Layer 

The application lAyer allows end systems to communicate with _Interprocess communication (IPC)_ 

This is done through the use of _sockets_ 

Each socket has a _port_ and an _IP address_ 

## Application Layer Protocol | HTTP(s) 
### HTTP(s) | Performance 
Performance of HTTP is measured with **Page Load Time (PLT)** 
* +Caching and representation 
* +Better DL speed with better HTTP by requesting smaller objects 
* +Take advantage of Webhosting and Data Center's Economy of scale 

### HTTP(S) | Persistence 
No persistance means that the connection between the client and server is shortlived. It dies after a query and response. _RTT is doubled as a result_

Persistance means the connection is maintained and stays alive until either the server or client closes it. 
### HTTP(S) | Pipelining/Non-pipelining 
Pipelining: Data is sent all at once, and then the client awaits for a response 
Non-Pipelining: ACK must be received before the next segment is sent. 
### HTTP(S) | Caching (CDN) 
Caching uses local references to attain information without contacting the origin server. It reduces response time and traffic. 

It also helps "poor" content providers to deliver more effectively by spreading servers across the network. 

This is done through the usage of _last-modified-date_ and _E-tags_.  

## Application Layer Protocol | SMPT/IMAP
Also known as _simply mail transfer protocl_. 
* uses TCP for realiable transfer
* uses port 25 
* has 3 steps: 
    * handshaking 
    * transfer of messages
    * closure 
* Commands are in ASCII text 
* Responses contain a status code and a phrase
* If the other person is not on, the email is stored on the other person's mail server 

## Application Layer Protocol | HTTP(s) 
Will have in detail in another file.
