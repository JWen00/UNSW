# Domain Name System 

DNS is an application-layer protocol which contains a database of name servers and hosts. 

The database is implemented in _heirarchy_ of many name server. DNS has
* Hierarchical namespace
* Hierarchical administration 
* Hierarchical servers 

Services 
* hostname to IP address translation 
* host aliasing 
* mail server aliasing 
* distributes load with replicated web servers 

DNS is not centralised as it will create a single point of failure and will be difficult to maintain. 

DNS servers are replicated so queries can be load-balanced between replicas 

DNS uses UDP.

## DNS Query | Recursive 
A recursive query puts a burden of name resolution on the contact name server 

Servers caches its mappings so subsequent requests will be faster 

Caches entries will timeout and becomes out of date after a certain amount of time 

## DNS Query | Iterated 
Local DNS contacts a server and redirected to another server. Each query is saved and cached by the local DNS server unlike in Recursive queries. 

## DNS Records 
**Record Types | A**
* Name: hostname 
* Value: IP address 

**Record Types | CNAME**
* Name: alias name 
* Value: Canonical name

**Record Types | NS**

* Name: domain 
* Value: hostname 

**Record Types | MX**
* Value: name of mailserver associated with name 

## DNS Security | DDoS 

Denial of service => bombarding root servers with traffic or TLD servers 

Redirecting queries by intersepting or spoofing query source addresses 

## DNS Security | Cache Poisoning 

DNS servers which cache IP address may be redirected. We should avoid this 

