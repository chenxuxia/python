__author__ = 'cxx'
# -*- coding:utf-8 -*-
import urllib.error
import urllib.request
import re

#糗事百科爬虫类  https://github.com/516310189/PythonSpider
'''
正则表达式说明
1）.*? 是一个固定的搭配，.和*代表可以匹配任意无限多个字符，加上？表示使用非贪婪模式进行匹配，也就是我们会尽可能短地做匹配，以后我们还会大量用到 .*? 的搭配。

2）(.*?)代表一个分组，在这个正则表达式中我们匹配了五个分组，在后面的遍历item中，item[0]就代表第一个(.*?)所指代的内容，item[1]就代表第二个(.*?)所指代的内容，以此类推。

3）re.S 标志代表在匹配时为点任意匹配模式，点 . 也可以代表换行符。
'''
class QSBK:
   
    def __init__(self):
        '''初始化方法，定义一些变量'''
        self.pageIndex = 1
        '''
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360EE'
        #初始化headers
        self.headers = { 'User-Agent' : self.user_agent }
        '''
        self.header = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
		}
        self.url = "https://www.qiushibaike.com/hot/page/"
        #存放段子的变量，每一个元素是每一页的段子们
        self.stories = []
        #存放程序是否继续运行的变量
        self.enable = False


    def getPage(self,pageIndex):
        '''传入某一页的索引获得页面代码'''
        try:
            '''
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            #构建请求的request
            request = urllib.request.Request(url,headers = self.headers)
            #利用urlopen获取页面代码
            response = urllib.request.urlopen(request)
            #将页面转化为UTF-8编码
            pageCode = response.read().decode('utf-8')
            return pageCode
            '''
            request = urllib.request.Request(self.url + str(pageIndex), headers=self.header)
            respense = urllib.request.urlopen(request)
            return respense.read().decode('utf-8')

        except urllib.request.URLError as e:
            if hasattr(e,"reason"):
                print (u"连接糗事百科失败,错误原因",e.reason)
                return None
            '''
            print("getPage失败")
			if hasattr(e, "code"):
				print(e.code)
			if hasattr(e, "reason"):
				print(e.reason)
			return None
            '''

    def getPageItems(self,pageIndex):
        '''传入某一页代码，返回本页不带图片的段子列表'''
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print ("页面加载失败....")
            return None
        # 分组信息：1发布人，2段子的全部信息的部分地址， 3发布内容， 4发布图片， 5点赞数
        pattern = re.compile('''<div class="article block untagged mb15.*?<h2>(.*?)</h2>'''
							 + '''.*?<span>(.*?)</span>'''
							 + '''.*?<!-- 图片或gif -->(.*?)<div class="stats">'''
							 + '''.*?<span class="stats-vote"><i class="number">(.*?)</i>''', re.S)
        '''
        pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
        '''
        items = re.findall(pattern,pageCode)
        #用来存储每页的段子们
        pageStories = []
        #遍历正则表达式匹配的信息
        
        for item in items:
        	# 如果段子中没有图片, 去除<br/>
            if not re.search("img", item[2]):
                result = re.sub('<br/>', "\n", item[1])
                pageStories.append([item[0].strip(), result.strip(), item[3].strip()])    
            #是否含有图片
            '''
            haveImg = re.search("img",item[3])
            #如果不含有图片，把它加入list中
            if not haveImg:
                replaceBR = re.compile('<br/>')
                text = re.sub(replaceBR,"\n",item[1])
                #item[0]是一个段子的发布者，item[1]是内容，item[2]是发布时间,item[4]是点赞数
                pageStories.append([item[0].strip(),text.strip(),item[2].strip(),item[4].strip()])
            '''
        return pageStories       

    def loadPage(self):
        '''加载并提取页面的内容，加入到列表中'''
        #如果当前未看的页数少于2页，则加载新一页
        if self.enable:    # 2 中 == True:
            if len(self.stories) < 2:
                #获取新一页
                pageStories = self.getPageItems(self.pageIndex)
                #将该页的段子存放到全局list中
                if pageStories:
                    self.stories.append(pageStories)
                    #获取完之后页码索引加一，表示下次读取下一页
                    self.pageIndex+= 1


    def getOneStory(self,pageStories,page):
        '''调用该方法，每次敲回车打印输出一个段子'''
        #遍历一页的段子
        for story in pageStories:
            #等待用户输入
            recive = input()  #  2中raw_input()
            #每当输入回车一次，判断一下是否要加载新页面
            self.loadPage()
            #如果输入Q则程序结束
            if recive == "Q"or recive == "q":
                self.enable = False
                return
            #print (u"第%d页\t发布人:%s\t发布时间:%s\t赞:%s\n%s" %(page,story[0],story[2],story[3],story[1]))
            print("当前第:%s页\n发布人:%s\n内容:%s\n点赞数:%s\n" % (page, story[0], story[1], story[2]))


    def start(self):
        '''开始方法'''
        print ( "正在读取糗事百科,按回车查看新段子，Q退出")    
        #使变量为True，程序可以正常运行
        self.enable = True
        #先加载一页内容
        self.loadPage()
        #局部变量，控制当前读到了第几页
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                #从全局list中获取一页的段子
                pageStories = self.stories[0]
                #当前读到的页数加一
                nowPage += 1
                #将全局list中第一个元素删除，因为已经取出
                del self.stories[0]
                #输出该页的段子
                self.getOneStory(pageStories,nowPage)

spider = QSBK()
spider.start()