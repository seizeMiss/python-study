import urllib3
import json

http = urllib3.PoolManager()

# response = http.request('GET', 'https://www.baidu.com')

# print(response.data)

response = http.request('POST', 'http://httpbin.org/post', fields={'world': 'hello'})

print(response.data)

jsonStr = response.data.decode('utf-8')
print(jsonStr)
data1 = json.loads(jsonStr)
print(data1, type(data1))

print(data1['form'])

