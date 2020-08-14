# Week 1 - Recon 

## The lecture 
..felt more like a talk, covering a number of different concepts in various details. 

* Thread Modelling ([watch this](https://www.youtube.com/watch?v=bDJb8WOJYdA
))

Fix low-hanging fruit first - delete unnecessary content and restrict access 
* HTTP Requests 
* DNS
* Subdomains 
* Proxys
* Enumerating Content - Active (Trying combinations) Passive (Watching your url) 
* Sniff testing - checking out how secure the website is
### On proxys 

This is something I didn't know. 

Proxies exist to mark your identity to the server.

Proxies can load balance, cache data in order to save time. They can also allow bad people to intercept your requests. 

Reverse proxies mean that the client doesn't know which server they're getting. This is useful for when a big domain has multiple servers and they are redirected anoniously to help load balance or test new services. 

In getting started, we are required to set up a proxy. Honestly I just trusted the website and downloaded the proxy. The way it was done, was through email verification and then a password verification when installing the proxy. 

So what we now have, is a certificate which recognises me, the user everytime I access quokkabank.com. 

Then, we needed to sign in by changing the values within the site. Ahhhhh. 

### On Subdomains 

Subdomains are created to organise and navigate different sections of a website. 

Particular domains may not be accessible to the public. 

A vulnerability may exist when a user finds a page they should not have access to. 

This week's challenge involves **Finding as many subdomains as you can**.

To find subdomains you can use online [pen-testing tools](www.pentest-tools.com). Results. 

* dev.quokkabank.com 
* *.quokkobank.com 

My dumb ass accidently closed the tab and this site only allows you to scan twice. 

This is probably because they run thousands of words as tests to see if the subdomain exists - otherwise known as brute forcing. 


It is also possible through manual searching in the terminal .

`dig quokkabank.com` 

```              
;; ANSWER SECTION:
quokkabank.com.         195     IN      A       184.168.221.57

;; AUTHORITY SECTION:
quokkabank.com.         3195    IN      NS      ns19.domaincontrol.com.
quokkabank.com.         3195    IN      NS      ns20.domaincontrol.com.

```

` dig @ns19.domaincontrol.com quokkabank.com axfr` 

```
;; communications error to 2603:5:21d0::a#53: end of file

;; communications error to 2603:5:21d0::a#53: end of file
```

Mine didn't work.. but supposedly AXFR (Authoritative transfer) which makes the client a "slave server" requesting data from a "master server." 