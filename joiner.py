import httpx
import requests
import random
import json
import threading
import string
proxies = []
usernames = []
domains = ["@gmail.com", "@yahoo.com", "@outlook.com"]
randomly_gen_usernames = False
print("Generator Made by: Pr0t0n X ADylan")
threads = input("Enter amount of threads you would like: ")
invite_link = input("Enter the invite code: ")
water_mark = input("Enter a watermark: ")
char_symbols = ["!", "@", "#"]
with open('proxies.txt', 'r+') as f:
    proxiess = f.readlines()
    for proxy in proxiess:
        proxy = proxy.replace("\n", "")
        proxies.append(proxy)

with open("username.txt", 'r+') as f:
    data = f.readlines()
    lines = 0
    for username in data:
        lines += 1
        usernames.append(username)
    if lines == 0:
        randomly_gen_usernames = True
        print("[+]: No Usernames Detected in file, Now Randomly Generating Usernames")

def generate_username(length: int):
    print("[+]: Generated Username")
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

def generate_passwords(length):
    return ''.join(random.choice(string.ascii_letters) for x in range(int(length))) + random.choice(char_symbols)

def generate_email(length):
    print("[+]: Generated Email")
    return ''.join(random.choice(string.ascii_letters) for x in range(int(length))) + random.choice(domains)
    


def fetch_cookies(proxy):
    print("[+]: Fetching Cookies")
    url = 'https://discord.com/register/'
    session = requests.Session()
    session.proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    data = session.post(url)
    cookies = data.cookies.get_dict()
    dcfduid = cookies.get('__dcfduid')
    sdcfduid = cookies.get('__sdcfduid')
    session.close()
    print(f"[+]: Fetched dcfduid {dcfduid[:10]}... and sdcfduid {sdcfduid[:10]}... Cookies")
    return dcfduid, sdcfduid

def solve_captcha(proxy):
    print("[+]: Solving Captcha")
    captchakey = httpx.post("http://ezcaptcha.us:8080/solvecaptcha", json={
        "site_key": "4c672d35-0701-42b2-88c3-78380b0db560",
        "site_url": "https://discord.com/",
        "proxy_url": proxy
    }, timeout=None)
    captchakey = captchakey.text
    captchakey = str(captchakey)
    if "unable" in captchakey.lower():
        print("[+]: Error Solving Captcha")
        return join_server()
    print(f"[+]: Solved Captcha {captchakey[:10]}")
    return captchakey

def get_fingerprint(proxy):
    print("[+]: Fetching Fingerprint")
    session = requests.Session()
    url = 'https://discord.com/api/v10/experiments'
    session.proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    data = session.get(url)
    fingerprint = data.json()['fingerprint']
    print(f"[+]: Fetched Fingerprint {fingerprint[:10]}...")
    return fingerprint


def join_server():
    proxy = random.choice(proxies)
    proxy = proxy.replace("\n", "")
    if randomly_gen_usernames == True:
        username = generate_username(random.randint(8, 12))
    else:
        username = random.choice(usernames)
    username += " | "
    username += water_mark
    username = username.replace("\n", "")
    password = generate_passwords(random.randint(10, 16))
    email = generate_email(random.randint(8, 12))
    dcfduid, sdcfduid = fetch_cookies(proxy)
    fingerprint = get_fingerprint(proxy)
    captcha = solve_captcha(proxy)
    url = 'https://discord.com/api/v10/auth/register'
    session = requests.Session()
    session.proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    headers = {
                "accept" : "*/*",
                "accept-encoding" : "gzip, deflate, br",
                "accept-language" : "zh-CN,zh;q=0.9,en;q=0.8",
                "content-type":"application-json",
                "cookie":f"__dcfduid={dcfduid}; __sdcfduid={sdcfduid}; _gcl_au=1.1.33345081.1647643031; _ga=GA1.2.291092015.1647643031; _gid=GA1.2.222777380.1647643031; OptanonConsent=isIABGlobal=false&datestamp=Fri+Mar+18+2022+18%3A53%3A43+GMT-0400+(%E5%8C%97%E7%BE%8E%E4%B8%9C%E9%83%A8%E5%A4%8F%E4%BB%A4%E6%97%B6%E9%97%B4)&version=6.17.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __cf_bm=.fksdoBlzBs1zuhiY0rYFqFhDkstwwQJultZ756_yrw-1647645226-0-AaluVZQHZhOL5X4GXWxqEIC5Rp3/gkhKORy7WXjZpp5N/a4ovPxRX6KUxD/zpjZ/YFHBokF82hLwBtxtwetYhp/TSrGowLS7sC4nnLNy2WWMpZSA7Fv1tMISsR6qBZdPvg==; locale=en-US",
                "origin":"https://discord.com",
                "referer":"https://discord.com/register",
                "sec-ch-ua" : "Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99",
                "sec-ch-ua-mobile":"?0",
                "sec-ch-ua-platform":"macOS",
                "sec-fetch-dest":"empty",
                "sec-fetch-mode":"cors",
                "sec-fetch-site":"same-origin",
                "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
                "x-discord-locale": "en-US",
                "x-fingerprint": fingerprint,
                "x-super-properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJ6aC1DTiIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85OS4wLjQ4NDQuNzQgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijk5LjAuNDg0NC43NCIsIm9zX3ZlcnNpb24iOiIxMC4xNS43IiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjExOTc2MSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
    }

    payload = {
        "fingerprint": fingerprint,
        "email": email,
        "username": username,
        "password": f"Pr0XDy{password}?",
        "invite": invite_link,
        "consent": True,
        "date_of_birth": "1999-05-05",
        "gift_code_sku_id": None,
        "captcha_key": captcha
    }

    data = session.post(url, headers=headers, json=payload)
    if int(data.status_code) == 201 or int(data.status_code) == 200:
        token = data.json()['token']
        print(f"Created Account and Joined Server with token {token[:10]}...")
        return join_server
    else:
        print(f"An Error Occured While Creating account or joining Server\nPossible Invalid Captcha Response!\nResponse: {data.text}")
        return join_server
        
if __name__ == "__main__": 
    for i in range(int(threads)):
        threading.Thread(target=join_server).start()
