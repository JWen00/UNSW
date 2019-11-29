# COMP3331 Lab02 

>Http & Socket programming 

## Exercise 1: using Telnet to interact with Web sever

### 1.1 `GET / HTTP/1.1` 

Response Type: HTML 
Response Size: 4839 (Bytes)
Accept-Ranges: None 
Last-Modified: Thursday, 1st November 2018

TODO: What is the acceptance range used for. 

### 1.2 `HEAD / HTTP/1.1`

Head returns just the header files, without any content. 
Response Type: HTML 
Response Size: 4839 (Bytes)
Accept-Ranges: bytes 
Last-Modified: Thursday, 1st November 2018

### 1.3 Get people.html

This was done through the following commands: 
```
$ telnet vision.ucla.edu 80 
GET /people.html HTML/1.1 
host: www.vision.ucla.edu
```

### 1.4 Why do we need GET? 

GET is part of the HTTP request message, together, GET and POST determine whether we're retrieving or giving information to the server. 

## Exercise 2: Understanding Internet cookies 

```
$telnet www.google.com.au 80
GET / HTML/1.1
host: www.google.com.au
```
### 2.1 Does Google set cookies (Telnet)?

Yes it does. there is a section in the header file which tells us:

```
Set-Cookie: 1P_JAR=2019-09-20-03; expires=Wed, 30-Oct-2019 03:39:46 GMT; 
```

### 2.2 Does Google store cookies (Browser)

``` 
1. Open Firefox and clear cookies 
2. Open www.google.com 
3. Check cookies 
```
There are now 6 cookies: 
* 4 from google.com 
* 1 from google.com.au
* 1 from doubleclick.net

### 2.3 Does Ucla store cookies?
 
 I didn't get any cookies stored.. 


## Exercise 3: Using Wireshark to understand basic HTTP request/response messages 

### 3.1 Status Code 

Status Code: 200 OK 

This means that everything was retrieved and all is good. 

### 3.2 HTML File Anlysis 
```
Last Modified: Tuesday, 23rd September 2003 

Date: Tuesday, 23rd September 2003 
```
Date is the date which the page is requested.

Last modified is when the page was last modified by the admin.

### 3.3 Persistant Connections

The page is NOT persistent as there are no cookies set in the return packet. 

### 3.4 Packet Size 

There are 73 bytes of content being returned ot the browser.

### 3.5 Packet Data

73 Bytes of text/html; charset=ISO-8856-1

## Exercise 4: Using Wireshark to understand the HTTP CONDITIONAL GET/response interaction

### 4.1 "IF-MODIFIED-SINCE" (Request 1)
_"If-modified-since"_ header is not there. 

### 4.2 Last Modified 

The response contains the last time the requested files are modified (23rd September 2003 5:35:00) 

### 4.3 "IF-MODIFIED-SINCE" (Request 2) 

If-Modified-Since contains the last modified time obtained when we last visited the website, 23rd September 2003 5:35:00.

### 4.4 E-Tags 

The first and second response contain the same ETag.
```
ETag: "1bf2f-173-8f4ae900" 
```

ETag's are used to check if the page has been cached before so that it can be loaded quickly. If it has not been seen before, then the ETag is added to the local cache. 

## Exercise 5: Ping Client