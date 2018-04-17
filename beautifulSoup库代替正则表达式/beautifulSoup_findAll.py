from bs4 import BeautifulSoup

html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

soup = BeautifulSoup(html,'lxml')
print(soup.find_all(text='Foo'))  #text

'''
find_all(name,attrs,recursive,text,**kwargs)
可以根据标签名，属性，内容查找文档

print(soup.find_all('ul')) #name的用法
for ul in soup.find_all('ul'):
    print(ul.find_all('li'))
print(type(soup.find_all('ul')[0]))


print(soup.find_all(attrs={'class': 'element'}))#attrs
print(soup.find_all(attrs={'id': 'list-1'})) 



find(name,attrs,recursive,text,**kwargs)
find返回的匹配结果的第一个元素

其他一些类似的用法：
find_parents()返回所有祖先节点，find_parent()返回直接父节点。
find_next_siblings()返回后面所有兄弟节点，find_next_sibling()返回后面第一个兄弟节点。
find_previous_siblings()返回前面所有兄弟节点，find_previous_sibling()返回前面第一个兄弟节点。
find_all_next()返回节点后所有符合条件的节点, find_next()返回第一个符合条件的节点
find_all_previous()返回节点后所有符合条件的节点, find_previous()返回第一个符合条件的节点
'''


