import requests
from bs4 import BeautifulSoup
#import urllib.request
import re 
import urllib
import urllib.error
import time

class BDTB:


    def __init__(self,baseUrl,seeLZ):

        self.baseurl = baseUrl
        self.seelz = '?see_lz='+str(seeLZ)
        # 将读取的内容写如的文件
        self.file = None
        self.floor=1

    def getPageCode(self,pageNum):
        '''
        获取当前页编码html
        '''
        url = self.baseurl +self.seelz + '&pn=' + str(pageNum)
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360EE'
            }
        #代码在一起
        request = urllib.request.Request(url,headers=headers)
        response=urllib.request.urlopen(request)
        return  response.read().decode('utf-8')
        '''        
        response=requests.get(url,params=headers)       
        #格式化html代码
        html=response.text
        soup = BeautifulSoup(html,'lxml')
        print(soup.prettify()) 
        '''


    def getTitle(self,html):
        '''
        获取帖子名
        '''
        pattern=re.compile('<h3.*?>(.*?)</h3>') #将正则表达式编译成正则表达式对象,方便复用该正则表达式
        result=re.search(pattern,str(html)) #扫描整个字符串返回第一个成功匹配的结果
        return result.group(1)
        
    
    def getPageNums(self ,html):
        '''
        获取总页数
        '''  
        pattern=re.compile('回复贴，共.*?>(.*?)<') 
        result=re.search(pattern,str(html)) 
        return result.group(1)

    
    def getConcent(self,html):
        pattern=re.compile('d_post_content j_d_post_content.*?>(.*?)</div>')
        result=re.findall(pattern,html)
        return self.clearImage(result)
    
    def clearImage(self,result):
        contents=[]
        for content in result:
            item=re.sub(re.compile('<img.*?>|<br>'),"\n",content)
            item=re.sub(re.compile('<a href.*?>|</a>')," ",item)
            contents.append(item.strip())#移除字符串头尾指定的字符(默认为空格)
        return contents

    def writeToFile(self,title,content):
        self.file=open(title+".txt","a") #wa会覆盖
        
        for item in content:
            self.file.write("\n"+"楼层"+str(self.floor)+"---"*15+"\n")
            self.file.write(item+"\n")
            self.floor+=1
         

    def start(self):
        html=self.getPageCode(1)
        title=self.getTitle(html)
        pageNum=self.getPageNums(html)       
        for num in range(int(pageNum)):
            if num>1:
                time.sleep(5)
            pageHtml=self.getPageCode(num+1)            
            content=self.getConcent( pageHtml)
            self.writeToFile(title,content) #写入文件

       
baseurl = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseurl,1)
bdtb.start()
