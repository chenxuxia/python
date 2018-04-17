from bs4 import BeautifulSoup
import requests
import random

def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list

def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies

if __name__ == '__main__':
    url = 'http://www.xicidaili.com/nn/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360EE'
                       
    }
    ip_list = get_ip_list(url, headers=headers)
    proxies = get_random_ip(ip_list)
    print(proxies)

'''
    函数get_ip_list(url, headers)传入url和headers，最后返回一个IP列表，列表的元素类似42.84.226.65:8888格式，
这个列表包括国内髙匿代理IP网站首页所有IP地址和端口。
    函数get_random_ip(ip_list)传入第一个函数得到的列表，返回一个随机的proxies，这个proxies可以传入到requests的get方法中，
这样就可以做到每次运行都使用不同的IP访问被爬取的网站，有效地避免了真实IP被封的风险。proxies的格式是一个字典：{‘http’: ‘http://42.84.226.65:8888‘}。

运行上面的代码会得到一个随机的proxies，把它直接传入requests的get方法中即可。
'''
web_data = requests.get(url, headers=headers, proxies=proxies)


proxies11= {
    proxies 
}
response  = requests.get("https://www.baidu.com",proxies=proxies11)
print(response.text)