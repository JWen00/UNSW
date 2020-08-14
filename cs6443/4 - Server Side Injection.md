# Server Side Injection  

## Outline 
* SSRF (Server Side Request Forgery) 
* Files/File Upload/Logs
* Executing Commands
* Includes
* Forward and Reverse Shells 
* Reverse Shells, TTY Cleanup 

## Server Side Include Variants 
* A:\ 
* http://
* gopher:// (and other non-http) 
* \\blah\ (UNC path) 
* localhost (and other host names) 
* ::1 (ipv6) 
* Local Web Services 

## SSRF 

Server-side requet forgery refers to when an attacker induces a server-side application to make HTTP requests not intended by the user. 

Some common examples include: 
* Causing the server to make a connection back to itself or a third parting system 
* Causing a user to reveal their password by mimicing the password reset site 
* URLs containins XML data
* [Blind SSRF](https://portswigger.net/web-security/ssrf/blind) - Blind SSRF vulnerabilities arise when an application can be induced to issue a back-end HTTP request to a supplied URL, but the response from the back-end request is not returned in the application's front-end response.


### Common SSRF Defences include 
* Blacklist-based input filters 
* Whitelist-based input filters
* Disable internal domains 
* Disable internal IPs 
* Aka Protect your infrastructure 




Commnd injection 
10.10.10.1; id
x``
$(id) 
id; ls 
return 
id; cat index.php
../../../../etc/passwd
Anything that the website is running as, as long as it has the permissions, you can run system commends 

uploading php webshells 
winterwolf 

ServerSide Request Forgery (SSFR)
Make requests through another website so that the end server thinks that it is safe

XML External Entity
Has a concept of entites -> variables 
You can store a value in an entity and then that entity is referenced 

You can inject an entity that gets files from  another place 

lsass.exe 
Local security Authority subsystem 

You can dump the memory
getting the registory.txt 

Mimikatz 