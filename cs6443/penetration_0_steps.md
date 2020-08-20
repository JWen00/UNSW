# Initial Recon 

Calm. Don't panic. 

## 1) What does the site do? 

Look at the page source. What is the structure. Take in all the information revealed. 

Look at the all the source files. Are there any hidden directories? 

Can even look for flags on the page and page source (xd) 

## 2) Look at the HEADERS and COOKIES 

Do they give out any information? 

Cookies may be in encrypted in base64/32/12/4 

Cookies may contain a JWT. 

Hashes are the same length no matter what. Lengths are a good indication of what hash it is. 


## 3) Check out `robots.txt`

Does robot.txt contain any other directories? 

## 4) Easy Logins 

Don't forget to check the obvious admin:admin or admin:password 

## 5) XSS? 

See steps on [xxs penetration](./penetration_XSS.md);

## 6) SSRF? 

See steps on [SSRF penetration](./penetration_SSRF.md);

## 7) XML? 

See steps on [XML penetration](./penetration_XML.md);

## 8) Latex?? 

 https://solutions.quoccabank.com/topic3

## See, you've learn alot 

* Identify hosts and file/paths in a site (IDOR) 
* Intercept and modify requests and reponses 
* On the browser, set JS breakpoint, modify DOM directly
* Exfiltrate cookies via XSS 
* Test and exploit SQLi 