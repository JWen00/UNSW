# Link Layer 

Packets in this layer are called _frames_. 

MAC addresses (Media Access Control) are the addresses of the card that makes it possible to connect to the internet. (Network adaptors). 

Your IP address is translated into a MAC address and vic-versa. 

## Link Layer Services 

The link layer is responsible for transferring data in a wide area network or in the local area network. 

* sending side: changes the datagram into frames (+header, +trailer channel access, +bit-checks) 
* sending side: looks for errors/flow control and then extracts datagram 
* reliable delivery between adjacent notes 
* flow control
* error detection & correction 
* half-duplex and full-duplex 

On the sending side, the datagram is made into a frame

## Framing in Ethernet 

Structure: 

* 7-byte Preamble: `1010101010`
* 1-byte SFD: `10101011` 
* 6-byte Dest MAC 
* 6-byte Source MAC 
* 2-byte Type/Length 
* 46-1500 Byte Payload 
* 4-byte FCS/CRC 
* Interfram Gap 12 bytes of idle state (depends on the speed) 

## Error Checking 

1. Parity checking - 2D check 
2. CRC Checking 

Sender: 

* Extend Data D with R zeros 
* Divide by generator G 
* Keep remainder R and adjust R checkbits  

Receiver: 

* Divide and check for 0 reminder 

## Multiple Access Protocol 

This is an algorithm that determines how nodes (endpoints) share the channel.

The problem being, communication about the channel involves using the channel itself. 

An ideal multiple access protocol: 

1. When one nodes wants to transmit, it can send at the broadcast channel rate 
2. When M nodes want to transmit, each node can send at the same rate 
3. The system is fully decentralised (as that would cause a single point of failure) 
4. Simple

### MAC Protocols | Channel Partitioning

1. TDMA (Time Division, Multiple Access) 

Access to the channel is given to each node in "rounds". Unused slots go idle

2. FDMA (Frequency Division Multiple Access) 

The channel spectrum is divided into frequency bands and each station is assigned one. (not good!?!?!)

Channel Partitioninng overall is food efficient at high loads (since there's less wasted space) 

### MAC Protocols | Random Access 

1. Slotted ALOHA 

When a node obtains a new frame, it transmits in the next slot. If there is a collision, it retransmits in each subsequent slot with a probability _p_ until success. 

This is good because a single node can transmit at the channel's full rate. It is highly decentralised and simple. 

However, this is collision prone, wastes slots and requires clock synchronisation. 
If we calculate for max efficienty, this protocol only uses the channel for useful transmissions 37% of the time. 

2. ALOHA 

Unslotted ALOGA requires no synchronisation. 

When the frame arrives, it transmits immediately. This is even workse, with  only 18% efficiency... Wait what.


3. CSMA/CD and CSMA/CA (used in wireless networks)

Nodes attempt to avoid collisions by beginning transmission only after the channel is sensed to be idle. 

When the sender senses that the channel is not idle, it backs off for a random amount of time before transmitting again. Each time it gets rejected, it waits for a longer interval. 

CSMA/CD requires a minimum packet size in order to give a host enough time to detet collisions. If the minimum size in not reached, the adaptor pads it until it has enough (46bytes) 

Random Access Protocols are not good for high loads as there's high collision probabilities 


### MAC Protocols | Taking Turns 

Taking turns looks for the best of Channel Partitioning and Random Access! 

1. Polling 

A master node invites a 'slave' node to transmit in turns 

This has a high overhead, high latency and single point of failure

2. Token Passing 

Control token is passed around as a key to being able to send. 

Single point of failure 

## Switched Lans 
dlfnslkdfnlskdnflksdnflskdnflsdknfsldkfnsldkfnsldknflskdnfdf

https://webcms3.cse.unsw.edu.au/COMP3331/19T3/resources/31954 
TODO: 
