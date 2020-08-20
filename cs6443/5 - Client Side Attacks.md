#  Client-Side Attacks 

* CSRF 
* Response Splitting 
* CSP 
* SOP 

## CSRF 

Cross-Site Request Forgery refers to when an attacker tricks the client into executing unwanted actions on a web application they're authenticated in. 

This attack can potentially obtain session details, authentication details or perform harmful actions. 

**An Example** could be building a URL or script and tricking the end user into clicking it. Clicking the link could appear harmless but it could potentially send a request to the intended servers under the identity of the user and authorise actions which the end-user did not intend to. 

**Preventions** include adding CSRF tokens for every request and/or for every session. Servers must verify the existence of the token in the request compared to the token found in the user's session. 

More on [owasp](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html#synchronizer-token-pattern)

## HTTP Reponse Splitting

Response splitting occurs when a HTTP response header is split into two pieces as a result of injecting an unsanitized “\r\n\r\n” sequence. This causes the latter half of the response to be parsed as part of the body content, possibly leaking header data into the web page.

It can be used to bypass CSP in the headers. (ahem report.quoccabank).

## Click Jacking 

Click jacking tricks the user into clicking hidden content. 

Attackers would copy the layout of a familiar website or embedd it within an iframe and add an object with 0 opacity on it so users are tricked into clicking the attacker's button instead of the real button. 

**Prevention** exists! (Thankfully) There are JS NoScript's which enfoce the current app window as top window and make all frames visible to prevent clicking on invisible frames. They are also capable of intercepting and flagging potential attacks to users. 

However, attackers can bypass NoScript's by using `allow-script` or `allow-forms`.

```html
<iframe id=”victim_website” src=”https://victim-website.com” sandbox=”allow-forms”>
</iframe>
```

To fix the root of this, we use CSP. 

## CSP 

Content Security Policy is a HTTP header within a response which specifies the loading of resources (scripts, imagees etc) such that only trusted locations are allowed. 

It is effective against XSS and Clickjacking. 

>
> In addition to restricting the domains from which content can be loaded, the server can specify which protocols are allowed to be used; for example (and ideally, from a security standpoint), a server can specify that all content must be loaded using HTTPS. A complete data transmission security strategy includes not only enforcing HTTPS for data transfer, but also marking all cookies with the secure attribute and providing automatic redirects from HTTP pages to their HTTPS counterparts. Sites may also use the Strict-Transport-Security HTTP header to ensure that browsers connect to them only over an encrypted channel.

 - Referenced from https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP

CSP can be specified within the HTTP header, `<meta>` tag.

A simple CSP header could be 
```
Content-Security-Policy: default-src 'self'; 
```

This means the site wants all the resources to come from the site's own origin (excluding subdomains). However this does not allow any scripts to run from anywhere else. This can be quite troubling. 

The site can then set the header to 
```
Content-Security-Policy: default-src 'self' *.trusted.com
```

which specifies which domains are trusted. 

A more specific policy could be 
```
Content-Security-Policy: default-src 'self'; img-src *; media-src media1.com media2.com; script-src userscripts.example.com
```

A **CSP Nonce** is an arbitrary number that can be used just once and added to script tag attributes in order to tell the browser a script is safe to be executed. 

For example, instead of having inline code specify the Nonce Token 

```
Content-Security-Policy: script-src ‘sha256-hWEXbex0cd37bsd3bspvnrDseE53=’;
```

Another method is to move the script to another file and allow that file to execute. 
```js
<script src="app.js”></script>
```

Or replacing
```js 
<button id="button1" onclick="doSomething()">
```
With this
```js
document.getElementById("button1").addEventListener(‘click’, doSomething);
```

## SOP 

Same Origin Policy ensures that javascript cannot access the data of another origin (cross-origin). 



The content must fulfil Scheme, Host and Port. For example 
```
http://mySite.com/dir2/other.html	[TICK]

http://mySite.com:81/dir/page.html  [TICK]	

http://notMySite.com/dir/page.html	 [BAD]

https://notMySite.com/dir/page.html	 [BAD]
```

Static content is not guarded by SOP, only Dynamic content. 

This is for client side trying to access a file on the server. When the client sends a request, it must also contain the headers which have same scheme, host and port. 

JSONP. 

In SOP world, all cross-origin calls must return with Access-Cosntrol-* headers: 
```
Access-Control-Allow-Origin: List of origins allowed
Access-Control-Allow-Methods: List of methods allowed
Access-Control-Allow-Headers: List of non-standard headers
Access-Control-Max-Age: Value in secs to cache preflight req
```
Aka, when you make a request, the server requests for those ^ header and compares the reports of that to the Access-Control-* headers. 