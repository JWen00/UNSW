# Wireless Networks 
There are two difficult challenges with today's wireless networks.

1. Communication in a noisy channel 
2. Handling changes between networks

## Wireless Links 

Consider two different types of wireless networks - one with infrastructure and one without. The difference being one has connection to the larger internet while the other relay to and only to each other. 

Diffferences to wired links: 

* Decreased signal strength 
* Interference from other sources 
* Multipath propagation - Packets arriving at different times due to reflection off objects. This can cause an access point to be unable to cover it's most ideal area 


### SNR VS BER tradeoffs 

SNR - Signal to noise (dB) 
BER - Bit Error Rate

[Look at graph] 

SNR may change dynamically to adapt with the power in the physical layer. 

### Hidden Terminal Problem 

Hidden terminal problem occurs when two nodes that are outside each other’s range performs simultaneous transmission to a node that is within the range of each of them resulting in a collision.

Data is lost from both parties due to a collision 

Hidden nodes means increased probablility of collion on the receiver end. 

Possible Solution: Have the receiving range smaller than the sensing range 

### Exposed Terminal Problem

Exposed terminal problem occurs when the node is within the range of a node that is transmitting and it cannot be transmitted to any node.
 
Exposed node means denied channel access unnecessarily which ultimately results in under-utilization of bandwidth resources.
It also results in wastage of time-resource.


## IEEE 802.11 wireless LANs ("Wi-Fi") 

In order, previous LANs have been called: 

* 802.11.b
* 802.11.a
* 802.11.g
* 802.11.n 

### CSMA/CA

All wireless LANs uses CSMA/CA for multiple access (Carrier-Sense multiple access with collision avoidance). This is a multiple access method where nodes attempt to avoid collisions by beginning transmission only after the channel is sensed to be idle. 

When the sender senses that the channel is not idle, it backs off for a random amount of time before transmitting again. Each time it gets rejected, it waits for a longer interval. 

Another idea is to 'reserve' the channel. A request (RTS) is sent, and when the channel is clear, the channel broadcasts a clear to send (CTS) that is heard by all notes. 

### 802.11.b

* is divided into 11 channels at different frequences (2.4GHz-2.48GHz) 
* host must associate with an _access point (AP)_ 
* AP scans channels, listening for frams containing the AP's name (SSID) and MAC address 
* AP runs DHCP to get the IP address in the AP's subnet
* passive and active scanning, one probes while the other doesn't 

All have a base-station and ad-hoc network version. 




