import requests

response = requests.get('https://www.baidu.com')

print(response.url)
print(response.content)
print(response.status_code)