import requests
'''
response = requests.get("http://www.baidu.com") #获取cookie
print(response.cookies)
for key,value in response.cookies.items():
    print(key+"="+value)


s = requests.Session() #模拟登陆，做会话维持
s.get("http://httpbin.org/cookies/set/number/123456")
response = s.get("http://httpbin.org/cookies")
print(response.text)


from requests.packages import urllib3 # 证书验证
urllib3.disable_warnings()

response = requests.get("https://www.12306.cn",verify=False)
print(response.status_code)

proxies= {
    "http":"http://127.0.0.1:9999",
    "https":"http://127.0.0.1:8888"
}  #代理设置
response  = requests.get("https://www.baidu.com",proxies=proxies)
print(response.text)


如果代理需要设置账户名和密码,只需要将字典更改为如下：
proxies = {
"http":"http://user:password@127.0.0.1:9999"
}
如果你的代理是通过sokces这种方式则需要pip install "requests[socks]"
proxies= {
"http":"socks5://127.0.0.1:9999",
"https":"sockes5://127.0.0.1:8888"
}
'''

#认证设置
response = requests.get("http://120.27.34.24:9001/",auth=("user","123"))
print(response.status_code)