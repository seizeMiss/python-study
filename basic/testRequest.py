import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
headers = {'User-Agent': ua.random}
proxies = {
    # "https": "https://117.114.149.66:55443"
}
response = requests.get(url="https://www.baidu.com", headers=headers, proxies=proxies, timeout=5)

print(response.url)
print(response.content)
print(response.status_code)