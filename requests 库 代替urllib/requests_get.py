import requests
import json


response = requests.get("http://www.baidu.com")
print(type(response.status_code),response.status_code)
print(type(response.headers),response.headers)
print(type(response.cookies),response.cookies)
print(type(response.url),response.url)
print(type(response.history),response.history)
'''
data = {
    "name":"zhaofan",
    "age":22
}
response = requests.get("http://httpbin.org/get",params=data) #使用params关键字传递参数 data为none,则结果同下
print(response.url)
print(response.text)


response = requests.get('http://httpbin.org/get')
print(response.text)


# 解析json,两者结果相同
print(response.json())
print(json.loads(response.text))
print(type(response.json())) #<class 'dict'>

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36  QIHU 360EE"
    #"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}  #chrome://version 获取
response =requests.get("https://www.zhihu.com",headers=headers)
print(response.text)
'''