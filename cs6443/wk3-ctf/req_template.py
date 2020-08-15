
# Kindly donated by github.com/featherbear

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
    "myDataThing": 2
}
requests.post("https://my.website/endpoint", proxies=proxy, data=urllib.parse.urlencode(params), verify=False, headers={
    "Content-Type": "application/x-www-form-urlencoded"
})