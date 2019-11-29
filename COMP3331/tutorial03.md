# 1. Types of Delays
Transmission = length of packet / bandwidth 
Propogation = length of link / speed
Processing = calculating bit errors using checksum and next hop lookup 
Queueing = Time whne waiting to be processed 
# 2. Calculating RTT 
## a) 1 HTML Files and 3 JPEGs using HTTP 1.0
There is non persistant TCP 
so 4 things being sent * 2 RTTs = 8 RTT 
## b) 1 HTML Files and 3 JPEGs using HTTP 1.1
Now, TCP is persistant and pipelined. 
1RTT + 1 RTT (HTML) + 1 RTT (JPEGs) 
