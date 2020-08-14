# Authentication and Authorisation  

**Overview** 

Authentication -> Session Management -> Access Control 

The questions we should be asking are: 

Is the user who they claim to be? 

Is it still that user? 

Does the user have the right permissions? 

---

**Research** 

Practice hacks - bWapp

AUTHENTICATION BYPASS - 

Cookie session management video - 

Token vs Cookie based sessions - Difference

---

## Revision | The journey of a request
0) You type in a web-link 
1) This gets turned into a HTTPS Request 
2) This requests gets sent to your local DNS 
3) If the DNS does not have access to the server, then it asks other DNS's 
4) Request gets routed back to you onto your screen 


## Web Authentication 

In today's web, authentication can be achieved through 
* Password reset via email 
* 2FA 
* Delegated SSO, Oauth 
* CAPTCHAs

## Authentication flaws 
 
### Complexity of Passwords 
Noone wants to remember complicated passwords. If we try to brute force, the success-rate is actually quite high. - Try  it with rainbow tables.

We can also look at the security within the transport layer protocol within the network stack. 

> Brief Revison: The transport layer includes TCP and UDP, responsible for packet delivery. (Either you ensure the other party has received the packet - using a secure connection, or to send the packet without caring whether it has been received or not) 


* guess smart by adding context 
* cewl - pulling words from a site to add context 
* rockyou.txt

### Default Credentials 
Lots of sites still use default credentials such as 
* admin/admin 
* admin/password
* admin/""
* guest/guest

Password Resets sometimes would include the required pin if you inspect the site! How scary D: 

### Secret Questions?? 
Secret questions may be reconed!! Very easily


### Revealing extra information

Reminding the user that they typed their password makes a great user interface but this tiny bit of information can greatly help a brute forcer who can continuously test passwords against that uesrname.

E.G. Extra information such as "Invalid Username" or "Invalid Password" and not both at the same time. 

A great way to prevent this is to block a user after a set amount of attemps. 

---
## Session Management Flaws 

### Session Creation 

How are sessions created? Can I fake my own session? 

Can I attack the PRNG and generate my own cookie? 

Can I "fixate" a session? 

### Session Handling / Transfer / Usage 

Can I steal the cookie through XSS (no 'httpOnly' flag?) 

Can I steal the cookie through redirecting to HTTPS? 

What information does the site trust the user to provide? 

### Session cleanup 

What happens when you click "log out"? - Fun fact! You never really log out :) 

Under what conditions is a session actually destroyed? What happens then? - Can you take advantage of this? 

Do sessions time out correctly?

### Understanding the structure of Sessions 

There is a difference between user session ID and browser session ID. 

E.G If you have a cart, it might save your items just in your browser. 

There are 3 levels of security - Strict, Relaxed, None. 

Bank sites do not retain any information as it is mostly sensitive. 

1. name=value (Data to store) 
2. Domain (Specifies the domain/subdomain the cookie belongs to)
3. Expiry Date (When should the cookie be deleted)
4. Secure (To only send cookies over a secure connection (HTTPS)) 
5. HttpOnly (Disable access to cookies from Javascript) 

The last one, you can still access your own cookies so if someone gets access to your physical computer, they can still steal it. 


### CSRF 

Cross-site request forgery is a one-click attack which steals your session by exploiting a website where unauthorised commands are transmitted from a user that the web application trusts. 

---

## Authorisation Flaws 

### Storing authorisation data on client side 

An example is storing authorisation details within cookies. Did you know this was actually very common in 1999 where cookies stored "usertype=admin" 

### Authorisation via URL parameters 

`.../php?admin=1`  

Very bad. 

### Time between logout and session expire
 
 









