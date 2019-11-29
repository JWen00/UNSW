# COMP3331 Lab04 

## Exercise 1 Understanding TCP using Wireshark 

### 1.1 `gaia.cs.umass.edu`

The IP address of `gaia.cs.umass.edu` is `128.119.245.12` 

It is sending on port 1161 and receiving on port 80.  

The IP address and port of the client computer is `192.168.1.102` on port 1161. 

### 1.2 TCP segment w/ HTTP POST command 

The sequence number containing the HTTP POST command is `232129013`

### 1.3/4 Segments after segment 232129013

#|SeqNo|Time Sent|Time ACK'd|RTT|Est. RTT|Length|
|:-:|:----:|:---:|:---:|:---:|:---:|:---:|:---:|
4|232129013|0.026|0.053 #6|0.027|0.027|565
5|232129578|0.041|0.077 #9|0.036|0.028|1460
7|232131038|0.054|0.124 #12|0.07|0.04|1460
8|232132498|0.056|0.169 #13|0.113|0.049|1460
10|232133958|0.077|0.217 #15|0.14|0.0.06|1460
11|232135418|0.078|0.267 #16|0.189|0.07|1460

### 1.5 Min buffer space

The minimum buffer space is 16384. It doesn't throttle the sender because the max length being sent is 1514 bits long. 

### 1.6 Retransmitted segments 

Yes there are multiple instances where the ACKs from servers have been retransmitted. I checked for repeated sequence numbers to find the retransmissions of packets. 

### 1.7 ACKs 
How much data does the receiver typically acknowledge in an ACK? Can you identify cases where the receiver is ACKing every other received segment (recall the discussion about delayed acks from the lecture notes or Section 3.5 of the text)

There is a case where between packet 59 and 62, it acks every second packet (54-57)

### 1.8 Throughput 

Throughput  
= bytes / time  
= (First SeqNo - last ACK) / (Last Seg time - first ack time)  
= (232293103 - 232129013) / (5.6511 - 0.026)   
= 164090 / 5.55661  
= 28903.84 bytes/sec

## Exercise 2: TCP Connection Management 

### 2.1 SeqNo for Initiation 

SYN SeqNo is `2818463618` 

### 2.2 SeqNo for SYNACK 

SYNACK SeqNo is `1247095790`

ACK value in the SYNACK is `2818463618`. This is determined by the SYN SeqNo +1. (Applies to all SYNs) 

### 2.3 SeqNo of ACK by Client 

SeqNo in response to the SYNACK is `2818463619`. The ACKNo is `1247095790`, the previous SeqNo +1 (Since we are replying to an SYNACK) All other acks do not increase by 1. 

Since this is an ACK, it does not contain any data. 

### 2.4 Who did the active close 

Client did the active close. We can tell because in segment number 304, the client sends the first FIN Segment. 

It is a simultaneous close. 

### 2.5 How many bytes of data? 

The amount of data sent can be calculated with the initial sequence number and the final ACK number -2 (since the SYN and FIN byte is not counted) 

Total data is `2818463618` - `2818463653` - 2 = 33








