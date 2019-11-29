# Network Layer 

## Responsibilities 

1. Forwarding packets from input to appropriate output  
2. Determining the route taken by packets from src to dest 

## Two planes | Data Plane & Control Plane 

Data Plane is local. (bottom of diagram) 

When a datagram arrives, it determines where the datagram is forwarded it to. 

Control plane is controls network-wide logic. (top)

It determines how datagrams are routed among routes by calculating end-to-end paths. Two methods of how this is determined: 

* Per-Router Control Plane - This is where every router knows every other router and interact with each other to compute a forwarding table. 

* Logically centralised control plane - A remote controller interacts with local control agents (CAs) to compute forwarding tables. 

> TODO: Probs going to go into more depth here 

## IP | Internet Protocol 

The IP manages the datagram's: 

### Format [Look at picture of Packet Structure]

* 8-bit protocol => tells end user how to handle the packet by identifying the Transport Protocol (TCP/UDP) 
* 8-bit TTL (Time to Live) => solves problems of packets stuck in loops. When a packet runs out of 'lives'
* 16-bit Checksum => Checks for header corruption
* 8-bit TOS (Type of Service) Allows packets to be treated differently.

### Fragmentation - solves the potential problem of having packets far too big 

When calculating, don't forget to calculate for the 20 byte IP header

Host checks the MTU (Max. Trasfer Size) by sending the big packet to all routers in the path (with a Do Not Fragment flag). Routers drop the packet if it's too large and provides feedback with ICMP message to tell the MTU. 

### IPv4 Addressing 

In IPv4, the IP address in seperated into the 'network' and 'host' part.

 (223.1.1.1 -> the last 1 is the host, indicated ports) 

A network is a set of device interfaces with the same network part of IP addresses, and can hence physically reach each other with intervening a router.


### Network Address Translation 

Networks are seperated into different classes (A, B, C) each having their own reserved set of available addresses. 

When translating the address, it is done through a series of tests to determine the class. 

Each class is also 'subnetted', dividing the class into 3 levels: 

* netid 
* subnetid
* hostid 

>>> Don't understand 

**CIDR: Classless InterDomain Routing**

Network portion of the address has an arbitary length 
Format: a.b.c.d/x, x is No. of bits in the network portion of address

**DHCP: Dynamic Host Configuration Protocol** 

DHCP is a method of obtaining an IP address from the network server when an end-system joins the network. 

```
Host: Broadcast "DHCP Discover" 
DHCP Server: "DHCP Offer" 
Host: "DHCP Request" 
DHCP Server: "DHCP ack" 
```

>>> Need more clarifycation

Want to watch the lecture on this. (Slide 58) 
