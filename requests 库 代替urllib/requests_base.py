import requests
response  = requests.get("https://www.baidu.com")
response.encoding="utf-8"


'''


print(type(response))
print(response.status_code)

print(response.text)
print(type(response.text))

print(response.cookies)

print(response.content)
print(response.content.decode("utf-8"))


'''
