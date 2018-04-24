'''
通过本地远程访问url，然后将url的读成源代码形式，然后对源代码进行解析，获取自己需要的数据，
相当于简单数据挖掘。本文实现的是将一个网页的图片爬出保存到本地的过程
'''
import requests
import urllib.request  
import re  
def get_html(url,data):
    '''
    :param url:请求的url地址
    :param data: 请求的参数
    :return: 返回网页的源码html
    '''
    response = requests.get(url,data)
    return response.text
'''  
改用requests，使用requests库代替urllib库
def getHtml(url):  
    page = urllib.request.urlopen(url)  ##打开页面  
    html = page.read() ##获取目标页面的源码  
    return html  
'''  
def getImg(html):  
    reg = 'src="(.+?\.png)"'  ##正则表达式筛选目标图片格式，有些是'data-original="(.+?\.jpg)"'  
    img = re.compile(reg)  
    imglist = re.findall(img, html) ##解析页面源码获取图片列表  
    x = 0  
    length = len(imglist)  
    for i in range(length):  ##取前6张图片保存  
        imgurl = imglist[i]   #'http://jingyan.shangxueba.com/images/logo.png'
        #代替!contain ,in 代替contain
        # "unknown url type: 'images/con_icon1.png' ——>" http://jingyan.shangxueba.com/images/app_bg.png
        if  imgurl.find("http" )==-1:
            imgurl ='http://jingyan.shangxueba.com/'+imgurl

        urllib.request.urlretrieve(imgurl,'F:\\taiyuan\\'+'%s.jpg' % x) ##将图片从远程下载到本地并保存 
        x += 1 
  
global Max_Num  
Max_Num = 2
##有时候无法打开目标网页，需要尝试多次，这里设置为1次  
for i in range(Max_Num): 
    base_url = "http://www.shangxueba.com/jingyan/2438398.html"
    data = {}
    try: 
        html = get_html(base_url, data) 
        #html = getHtml("view-source:http://www.shangxueba.com/jingyan/2438398.html") 
        #  
        getImg(html)  
        break 
    except Exception as e:  
        
        if i < Max_Num - 1:  
            continue  
        else:  
            print ('URLError:'+str(e))  