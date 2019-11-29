## What is the internet 

The internet is a network of networks containing: 
* End Systems _(e.g. phones, computers, laptops)_ 
* Routers connects different networks together 
* Switch redirects packets to their destination _(e.g. routers and link-layer switches)_ 
    * **Link layer switches** are used in access networks while routers are used in network cores
* Servers, a collection of computers which provides a service via the internet
* Modems connect two networks through an analogue link _(e.g.telephone cables)_

## End Systems 
End system are connected by **communication links** which can be:
* Coaxial Cable
* Copper wire 
* Optical fibre 
* Radio spectrum 

When a end system has data to send to another systems, it send the data in segments known as **packets**. Packets contain TODO: 

###  End systems access the internet through internet service providers (ISP). 

* ISP Examples include: local cables, telephone companies 
* ISPs in itself is a network of packet switches and communiation links
* ISPs provide internet through _residential broadband access, high-speed local area network access, wireless access and 56 kbps ial-up modem access_
* ISPs are separated into tiers: lower tiers connected through national and international upper-tier ISPs 
* High Tier ISPs include: _AT&T, spinrt and NTT_.  
* High Tier ISPs run with hish-speed fibre-optic links 

### TCP/IP Protocol 

The **Internet Protocol (IP)** specifies the format of packets that are send and received. 

RFC and IETF both contribute to resolve network and protocol design problems. 

## The Network Core

### Packet Switching

Most packet switches use **store-and-forward transmission**. This means the switch must receive the entire packet before it can begin to transmit again. 

For each attatched link, the switch has an **output buffer**. Hence, packets suffer **queueing delays** which depend on the congestion in the network. Since the buffer space if finite, when it is full, **packet loss** will occur.

### Further Analysis on delays

The total delay is calculated by adding all the possible delays. 
Delays which could be faced include:
#### Nodal processing delay

Time required to examine the packet header. Can inlcude the time required to check for bit-level errors. 

#### Queuing delay 

Time wasted in the buffer to be transmitted onto the commnucation link. 

#### Transmission delay

Time required to transmit all the packet's bits into the link 

#### Propagation delay 

Time required to transmit the data from link end of the link to another. This depends on the physical medium of the link _(e.g. fire optics, copper wire etc..)_ 


