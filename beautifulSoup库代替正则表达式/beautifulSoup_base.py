from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

soup = BeautifulSoup(html,'lxml')



print(soup.a.next_sibling )#获取下一个兄弟标签
print(soup.a.previous_sinbling) #获取上一个兄弟标签
print(soup.a.next_siblings) #获取后面的兄弟节点
print(soup.a.previous_siblings)#获取前面的兄弟节点

print(soup.a.paren)  #获取父节点
print(list(enumerate(soup.a.parents)))#获取祖先节点
print(soup.descendants) #获取子孙节点，结果是一个迭代对象，而不是列表，只能通过循环的方式获取素有的信息
for i,child in enumerate(soup.descendants):
    print(i,child)

print(soup.p.children) #获取子节点，结果是一个迭代对象，而不是列表，只能通过循环的方式获取素有的信息
for i,child in enumerate(soup.p.children):
    print(i,child)

print(soup.p.contents)

print(soup.head.title.string)
print(soup.p.attrs["class"])
print(soup.p["class"])
print(soup.title)
print(type(soup.title))
print(soup.head)
print(soup.p)
print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p["class"])
print(soup.a)
print(soup.find(id='link3'))
print(soup.find_all('a'))

for link in soup.find_all('a'):
    print(link.get('href'))

print(soup.get_text())



