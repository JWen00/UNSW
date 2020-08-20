# Brute Forcing 

Template 
```py
import re
import urllib
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

proxy = {
    'https': 'http://127.0.0.1:8080',
    'http': 'http://127.0.0.1:8080'
}

params = {
    "myKey": "myValue"
}
res = requests.post("https://my.website/endpoint", proxies=proxy, data=urllib.parse.urlencode(params), verify=False, headers={
    "Content-Type": "application/x-www-form-urlencoded"
})
```

To filter the output
```py
# encode the needle instead of the haystack incase there are invalid bytes in res 
needle = "string_to_encode".encode('utf-8') 
if needle in res.text: 
    print(res)
```