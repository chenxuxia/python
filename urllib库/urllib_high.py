'''
urllib.request.Request 使用
网站会需要携带一些headers头部信息才能访问，最长见的有user-agent参数，通过该模块添加
两种添加header信息的方法
'''
from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey' ,'name1': 'zhaofan'
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
'''

url = 'http://httpbin.org/post'
dict = {
    'name': 'Germey' ,'name1': 'zhaofan'
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, method='POST')
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
#这种添加方式有个好处是自己可以定义一个请求头字典，然后循环进行添加
'''