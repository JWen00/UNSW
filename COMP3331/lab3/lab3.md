# COMP3331 Lab03

## Exerise 1: Explore DNS records 

|Record Types|Description|
|:---:|:---:| 
|A| Address Record|
|CNAME|Alias of one name to another (Canonical Name)|
|MX|Mail Exchange record| 
|NS|Name Server Record| 
|PTR| Pointer to CNAME, but only returns name (Commonly used to reverse DNS lookups)|
|SOA| Stores the specific _authoritive_ information about a DNS Zone|
## Exercise 2: Tracing DNS with Wireshark
### 2.1 Transport Layer Protocol 
The transport layer protocol used is TCP. 
### 2.2 Source and Destination 
| |Source|Destination|
|:--:|:---:|:----:|
|Packet 5|3742|53|
|Packet 6|53|3742|
### 2.3 IP Address 
The query is being sent to `128.238.29.22`. It is always the local default DNS that is being used (as it is not specified)

### 2.4 Queries 
Observing the 5th and 6th packets, the query (5th packet) contains one "question" of type "A" which asks for the IP address of `mit.edu`. There are no answers in this packet. 

The answer (6th packet) contains the answer.  

### 2.5 DNS Response 

From the response message we can tell that: 
* the IP address for `mit.edu` is `18.7.22.83`
* it has 3 authoritative nameservers
    * BITSY.mit.edu (`18.71.0.3`) 
    * STRAWB.mit.edu (`18.71.0.151`) 
    * W20NS.mit.edu (`18.70.0.160`) 

## Exercise 3: Digging into DNS 

### 3.1 IP Address 
The IP address of `www.cecs.anu.edu.au` is `150.203.161.98`.

```
;; ANSWER SECTION:
www.cecs.anu.edu.au.	2786	IN	CNAME	rproxy.cecs.anu.edu.au.
rproxy.cecs.anu.edu.au.	1575	IN	A	150.203.161.98
```

This was found in the "ANSWER SECTION." A `CNAME` query was sent, which returned the alias `rproxy.cecs.anu.edu.au.`, which corresponds to the IP Address `150.203.161.98`.

### 3.2 Canonical Names 

The canonical name for `www.cecs.anu.edu.au` is `rproxy.cecs.anu.edu.au.` The alias may be used for the general public as it is much easier to remember `www.cecs.anu.edu.au` than `rproxy.cecs.anu.edu.au.`

### 3.1 Authority and Additional Sections

From the Authority Section we can infer that the server `rproxy.cecs.anu.edu.au` has authoritive name servers:
```
r.au 
d.au
t.au
a.au
c.au
v.au 
s.au 
u.au
q.au 
```


From the Additional Section we are given additional information on the IPv4 and IPv6 addresses of the authoritive name servers (so we can get to them if we need to) 

```
;; ADDITIONAL SECTION:
a.au.			6933	IN	A	58.65.254.73
a.au.			11247	IN	AAAA	2407:6e00:254:306::73
c.au.			12802	IN	A	162.159.24.179
c.au.			43849	IN	AAAA	2400:cb00:2049:1::a29f:18b3
d.au.			11630	IN	A	162.159.25.38
d.au.			100514	IN	AAAA	2400:cb00:2049:1::a29f:1926
q.au.			13089	IN	A	65.22.196.1
q.au.			9881	IN	AAAA	2a01:8840:be::1
r.au.			12140	IN	A	65.22.197.1
r.au.			96416	IN	AAAA	2a01:8840:bf::1
s.au.			5215	IN	A	65.22.198.1
s.au.			96416	IN	AAAA	2a01:8840:c0::1
t.au.			14111	IN	A	65.22.199.1
t.au.			96416	IN	AAAA	2a01:8840:c1::1
u.au.			38151	IN	A	211.29.133.32
v.au.			9031	IN	A	202.12.31.53
v.au.			11367	IN	AAAA	2001:dd8:12::53
```
### 3.4 Local Name Server
IP address of the local name server on my machine is `129.94.242.2` 

### 3.5 DNS Name Servers for `cecs.anu.edu.au` 
DNS Name Servers: `150.203.161.98`
IP Addresss is found in Additional Section 
```
;; ADDITIONAL SECTION:
ns2.cecs.anu.edu.au.	1344	IN	A	150.203.161.36
ns2.cecs.anu.edu.au.	1344	IN	AAAA	2001:388:1034:2905::24
ns3.cecs.anu.edu.au.	1338	IN	A	150.203.161.50
ns3.cecs.anu.edu.au.	1224	IN	AAAA	2001:388:1034:2905::32
ns4.cecs.anu.edu.au.	3455	IN	A	150.203.161.38
ns4.cecs.anu.edu.au.	662	IN	AAAA	2001:388:1034:2905::26
```
DNS Query: SOA   
### 3.6 IP Address `111.68.101.54`
The DNS name associated with `111.68.101.54` is `a.root-servers.net. nstld.verisi`

### 3.7 Dig for Yahoo! 

```
wagner %  dig @129.94.242.33 yahoo.com

; <<>> DiG 9.9.5-9+deb8u18-Debian <<>> @129.94.242.33 yahoo.com
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 6043
;; flags: qr rd ra; QUERY: 1, ANSWER: 6, AUTHORITY: 5, ADDITIONAL: 9

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;yahoo.com.			IN	A

;; ANSWER SECTION:
yahoo.com.		1800	IN	A	98.138.219.231
yahoo.com.		1800	IN	A	98.138.219.232
yahoo.com.		1800	IN	A	72.30.35.9
yahoo.com.		1800	IN	A	72.30.35.10
yahoo.com.		1800	IN	A	98.137.246.7
yahoo.com.		1800	IN	A	98.137.246.8

;; AUTHORITY SECTION:
yahoo.com.		43854	IN	NS	ns5.yahoo.com.
yahoo.com.		43854	IN	NS	ns2.yahoo.com.
yahoo.com.		43854	IN	NS	ns3.yahoo.com.
yahoo.com.		43854	IN	NS	ns1.yahoo.com.
yahoo.com.		43854	IN	NS	ns4.yahoo.com.

;; ADDITIONAL SECTION:
ns1.yahoo.com.		306842	IN	A	68.180.131.16
ns1.yahoo.com.		68167	IN	AAAA	2001:4998:130::1001
ns2.yahoo.com.		71477	IN	A	68.142.255.16
ns2.yahoo.com.		75491	IN	AAAA	2001:4998:140::1002
ns3.yahoo.com.		1727	IN	A	27.123.42.42
ns3.yahoo.com.		1727	IN	AAAA	2406:8600:f03f:1f8::1003
ns4.yahoo.com.		130918	IN	A	98.138.11.157
ns5.yahoo.com.		134116	IN	A	119.160.253.83

;; Query time: 144 msec
;; SERVER: 129.94.242.33#53(129.94.242.33)
;; WHEN: Sun Oct 13 21:54:59 AEDT 2019
;; MSG SIZE  rcvd: 388
```

As we can see in flags, we have `qr rd ra` but we do not have `aa`, so we did not get an authoritative answer. 

### 3.8 Dig for Yahoo! (using 150.203.161.36)

```
wagner %  dig @150.203.161.36  yahoo.com

; <<>> DiG 9.9.5-9+deb8u18-Debian <<>> @150.203.161.36 yahoo.com
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: REFUSED, id: 32501
;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;yahoo.com.			IN	A

;; Query time: 7 msec
;; SERVER: 150.203.161.36#53(150.203.161.36)
;; WHEN: Sun Oct 13 22:01:12 AEDT 2019
;; MSG SIZE  rcvd: 38
```
This query does not have an answer because we cannot tell another server (that is not CSE) to look for yahoo.com. 

### 3.9 Authoritative answer for Yahoo! mail 

```
wagner % dig @27.123.42.42 yahoo.com

; <<>> DiG 9.9.5-9+deb8u18-Debian <<>> @27.123.42.42 yahoo.com
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 53547
;; flags: qr **aa** rd; QUERY: 1, ANSWER: 6, AUTHORITY: 5, ADDITIONAL: 9
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1272
;; QUESTION SECTION:
;yahoo.com.			IN	A

;; ANSWER SECTION:
yahoo.com.		1800	IN	A	72.30.35.10
yahoo.com.		1800	IN	A	98.137.246.7
yahoo.com.		1800	IN	A	72.30.35.9
yahoo.com.		1800	IN	A	98.137.246.8
yahoo.com.		1800	IN	A	98.138.219.231
yahoo.com.		1800	IN	A	98.138.219.232

;; AUTHORITY SECTION:
yahoo.com.		172800	IN	NS	ns3.yahoo.com.
yahoo.com.		172800	IN	NS	ns4.yahoo.com.
yahoo.com.		172800	IN	NS	ns1.yahoo.com.
yahoo.com.		172800	IN	NS	ns2.yahoo.com.
yahoo.com.		172800	IN	NS	ns5.yahoo.com.

;; ADDITIONAL SECTION:
ns1.yahoo.com.		1209600	IN	A	68.180.131.16
ns2.yahoo.com.		1209600	IN	A	68.142.255.16
ns3.yahoo.com.		1800	IN	A	27.123.42.42
ns4.yahoo.com.		1209600	IN	A	98.138.11.157
ns5.yahoo.com.		1209600	IN	A	119.160.253.83
ns1.yahoo.com.		86400	IN	AAAA	2001:4998:130::1001
ns2.yahoo.com.		86400	IN	AAAA	2001:4998:140::1002
ns3.yahoo.com.		1800	IN	AAAA	2406:8600:f03f:1f8::1003

;; Query time: 402 msec
;; SERVER: 27.123.42.42#53(27.123.42.42)
;; WHEN: Sun Oct 13 22:13:17 AEDT 2019
;; MSG SIZE  rcvd: 388
```

An `A record` query is sent.


### 3.10 Simulate DNS query process 

```
1. dig .
2. dig @a.root-servers.net. au.
3. dig @162.159.25.38 edu.au
4. dig @65.22.196.1 unsw.edu.au
5. dig @129.94.0.192 cse.unsw.edu.au
6. dig @129.94.242.2 lyre00.cse.unsw.edu.au
=> lyre00.cse.unsw.edu.au.	3600	IN	A	129.94.210.20
```

The IP address is `129.94.210.20`. This took 6 queries. 

## 3.11 Can a machine have several names/IP address associated with it? 

You can have several name/IP addresses. However, it would require multiple network interface cards or virtual network IP name/IP addresses.(You can have two hostnames pointing to the same server.)