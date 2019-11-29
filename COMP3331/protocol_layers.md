# Protocol Layers 

Each layer has their own protocols; 
* Application _(HTTP(S) & FTP)_
* Transport _(UDP & TCP)_
* Network _(IP)_
* Link _(Ethernet, WiFi and the network's DOCSIS protocol)_
* Physical _(dependent on the physical cable)_

## Network Security 
#### 1. Run on different end systems 

We can run on different end systems using **Interprocess Communication** (IPC). One example is sockets: 

* Able to send/receive messages to/from its socket 
* Analogous to door as OS handles the details 

#### 2. Communicate over the network 

We can communicate through different networks, processes have and **identifier**. 

An identifier includes an _IP Address_ and _port numbers_. 

For example, a HTTP server has port number 80 while mail servers has port number 25. 

## Network Architectures 

### Client-Server Architecuter
### P2P Architexture

## Transport Services 

Requirements: 

#### 1. Data Integrity 

Does the app require 100% reliable data? 

For example file transfer requires every packet to be loaded while calls can tolerate some losses 

#### 2. Throughput 

Does the app require a minimum amount of throughput to be "effective"? 

Some apps can make use of whatever throughput they get 

#### 3. Timing 

Does the app require low delay, while some require extremely fast connections to be "effective" 

#### 4. Security 

### **Internet** protocol services 

Does the app require encryption and data integrity? 

Oh boi security!

#### TCP Service

* reliable transport
* flow control 
* congestion control (slows down the sender then network is busy)
* Does not provide timing, minimum throughput guarantee or security 
* connection oriented (setup is required between client and server) 


#### UDP Service 

* unreliable data transfer
* does not provide flow control, congestion control, timing, throughput guarantee security or orconnection setup 