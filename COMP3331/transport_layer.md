# Transport Layer 

The transport layer provides communication between app processes running on different hosts (end systems) 

## Multiplexing/Demultiplexing 

Multiplexing @ Senders: handle data from multiple sockets and then add a transport header on top.   

Demultiplexing @ Receiver end: user the transport header to deliver the received segments into the correct socket 

>For example, when a host received a UDP segment (of information), it checks the port number and directs it to the socket with that port number 

## Revision | Sockets 

A TCP socket is identified by 

* source IP address
* source Port Number
* destination IP address
* destination Port Number

A server host may support many TCP sockets simultaneously. 


## Connectionless Transport | UDP 

User Datagram Protocol is often known as the 'bare bones' of the internet transport protocol. This is because 

* segments often go missing
* or get delivered out of order to application layer
* doesn't have congestion management
* is "connection-less" as there is no hand-shaking 

However, this also means that UDP is be very fast as it does not need to worry about other factors. 

### UDP | Checksum

Checksum is used to detect bits which may have been flipped while being transmitted. 

The sender treats all the segment contents as 16-but integers and adds them together to put in the "checksum" field. 

The receiver then checks to see if any bits has been flipped. 

### UDP | Usage

UDP is typically used in _latency sensitive/time critical_ scenarios and/oor when error correction is unnecessary. 

* Quick request/response (DNS, DHCP) 
* Network Management
* Voice/Video Chat
* Gaming 

## Connection-oriented transport | TCP 

### TCP | Establishing a connection
Before establishing a connection and agreeing to send data, the sender and receiver performs a **"3-way handshake"**

```
// Client 
Socket clientSocket = newSocket("hostname", "portNo"); 

// Server 
Socket connectionSocket = welcomeSocket.accept() 
```

The initial segments are called **SYNBits**. When they are ACK'ed, the sequence number increases by 1. 

> NOTE: Server and Client chose their own sequence numbers, which are generated randomly 

``` 
Example
1. Client choses initial seqNo, 'x' 
2. Client sends a SYNbit with seqNo x 
3. Server choses initial seqNo y  
4. Server sends a SYNACK with ACKNumber x+1
5. Client receives the SYNACK and SYNACK's back with ACKNumber y+1 
```
> NOTE: The client/server knows that it has received a SYNBit from the **flags** section. Other flags include: ACK, FIN, RST, PSH, URG. 

If the SYNBit gets lost, the client has a timeout. Here is where we keep clicking refresh and it actually works!!

### TCP | Closing a connection 

There are 4 different ways to close the connection 

1. One at a time FIN, ACK, FIN, ACK 
2. Both Together FIN, ACK, _timed wait_ ACK 
3. Simultenous Closure FIN, FIN, ACK, ACK 
4. Abrupt Termination RST _(reset)_ => usually when the process on one end has crashed  

### TCP | Securi-tings 

* SYN Flooding - Constantly sending request connections but ghosting before sending the required ack! This happening at a large scale can easily overwhelm servers 
* TODO: TCP Cookies 

### Principles of reliable data transfer (RDT)
Making sure that the right data is received is highly important in the application, transport and link layers. 

To ensure RDT, we want to ensure only uni-directional data transfer by waiting for an ACK-knowledgement after every packet. 

Overview of the development of RDT 
* Error Free Transmission 
* Channel with bit-errors => use checksums 
* Transmission errors => ACKs and NAKs followed by retransmission 
* ACK or NAK corruptions => Add seqNo to each packet 
* Loss of packet and no response => sender waits for a "timeout" period 

### RDT | Pipelined Protocols 

RDT is not too bad but we can use pipelining to increase utilisation. (sending multiple at once and then waiting for a response) 

1. Go Back N 

Sender has up to N unacked packets and as a single timer for the oldest one. When the timer expires, retransmit all the unacked packets. 

There is no buffer so out of order packets are discarded. 

Receiver only sendss cumulative acks and does't ack if there has been a gap. 

2. Selective repeat 

Sender can have up to N unacked packets and maintains a timer for each unacket packet. When the timer for a packet expires, only that packet is sent. 

There is a buffer so packets can be accepted out of order. 

Receiver sends individual ack for each packet. 


### Principles of congestion control 

