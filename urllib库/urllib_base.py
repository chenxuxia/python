'''
Urllib是python内置的HTTP请求库
urllib.request 请求模块
urllib.error 异常处理模块
urllib.parse url解析模块
urllib.robotparser robots.txt解析模块
'''
import socket
import urllib.request
import urllib.error

try:
#parse
    data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
#通过bytes(urllib.parse.urlencode())可以将post数据进行转换放到urllib.request.urlopen的data参数中。这样就完成了一次post请求。

#urlopen 
#urllib.requeset.urlopen(url,data,timeout) 如果我们添加data参数的时候就是以post请求方式请求，如果没有data参数就是get请求方式

    response = urllib.request.urlopen('http://httpbin.org/post',data=data, timeout=1)
    print(type(response))  #响应类型
    print(response.read()) #获得的是响应体的内容
    print(response.status) #获取状态码
    print(response.getheaders())#头部信息
    print(response.getheader("server"))

except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
