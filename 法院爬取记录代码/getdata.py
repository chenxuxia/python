'''
目标地址：http://www.hshfy.sh.cn/shfy/gweb/ktgg_search.jsp
目标数据：目标地址页面的中间的案开庭公告数据

对数据页面分析
从打开页面后可以看到默认的数据是一个月的数据，即当天到下个月该天的
通过翻页可以返现这个时候页面的url地址是不变的，所以这里我们大致就可以判断出，中间表格的数据是通过js动态加载的，
我们可以通过分析抓包，找到真实的请求地址
'''

import requests
from bs4 import BeautifulSoup
import json
import time
import datetime
from config import *


def get_html(url,data):
    '''
    :param url:请求的url地址
    :param data: 请求的参数
    :return: 返回网页的源码html
    '''
    response = requests.get(url,data)
    return response.text


def parse_html(html):
    '''
    :param html: 传入html源码
    :return: 通过yield生成一个生成器，存储爬取的每行信息
    '''
    soup = BeautifulSoup(html, 'lxml')

    table = soup.find("table", attrs={"id": "report"})
    trs = table.find("tr").find_next_siblings()  #返回后面第一个兄弟节点。
    for tr in trs:
        tds = tr.find_all("td")
        yield [
            tds[0].text.strip(),
            tds[1].text.strip(),
            tds[2].text.strip(),
            tds[3].text.strip(),
            tds[4].text.strip(),
            tds[5].text.strip(),
            tds[6].text.strip(),
            tds[7].text.strip(),
            tds[8].text.strip(),
        ]

def write_to_file(content):
    '''
    :param content:要写入文件的内容
    '''
    with open("result.txt",'a',encoding="utf-8") as f:    # r'表示读' a  '已存在写入结尾，不存在创建'   with语句来自动帮我们调用close()方法,不再需要try 
        f.write(json.dumps(content,ensure_ascii=False)+"\n") 


def get_page_nums():
    '''
    :return:返回的是需要爬取的总页数
    '''
    base_url = "http://www.hshfy.sh.cn/shfy/gweb/ktgg_search_content.jsp?"
    date_time = datetime.date.fromtimestamp(time.time())
    data = {
        "pktrqks": date_time,
        "ktrqjs": date_time,
    }
    while True:
        html = get_html(base_url,data)
        soup = BeautifulSoup(html, 'lxml')
        if soup.body.text.strip() == "系统繁忙":
            print("系统繁忙，登录太频繁，ip被封锁")
            time.sleep(ERROR_SLEEP_TIME)
            continue
        else:
            break
    res = soup.find("div",attrs={"class":"meneame"})

    page_nums = res.find('strong').text
    #这里获得page_nums是一个爬取的总条数，每页是15条数据，通过下面方法获取总页数
    page_nums = int(page_nums)
    if page_nums %15 == 0:
        page_nums = page_nums//15   #// 取整除 - 返回商的整数部分
    else:
        page_nums = page_nums//15 + 1
    print("总页数：",page_nums)
    return page_nums


def main():
    '''
    这里是一个死循环爬取数据
    '''
    page_nums = get_page_nums()
    if not True:
        return
    base_url = "http://www.hshfy.sh.cn/shfy/gweb/ktgg_search_content.jsp?"
    while True:
        date_time = datetime.date.fromtimestamp(time.time())
        page_num = 1
        data = {
            "pktrqks": date_time,  #"ktrqks":
            "ktrqjs": date_time,
            "pagesnum":page_num
        }
        while page_num <= page_nums:
            print(data)
            while True:
                html = get_html(base_url, data)
                soup = BeautifulSoup(html, 'lxml')
                if soup.body.text.strip() == "系统繁忙":
                    print("系统繁忙，登录太频繁，ip被封锁")
                    time.sleep(ERROR_SLEEP_TIME)
                    continue
                else:
                    break
            res = parse_html(html)
            for i in res:
                write_to_file(i)
            print("爬取完第【%s】页,总共【%s】页" %(page_num,page_nums))
            page_num+=1
            data["pagesnum"] = page_num
            time.sleep(1)
        else:
            print("爬取完毕")
        print("开始休眠.......")
        time.sleep(SLEEP_TIME)
if __name__ == '__main__':
    main()
