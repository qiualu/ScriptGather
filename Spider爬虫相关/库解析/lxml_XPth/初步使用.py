

# 使用 lxml 的 etree 库
from lxml import etree


text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

# etree.HTML 初始化
html = etree.HTML(text)
result = etree.tostring(html)
print(result)   # 其打印出来

# lxml 因为继承了 libxml2 的特性，具有自动修正 HTML 代码的功能。 所以输出结果是这样的
# <html><body> .....

# 文件读取
from lxml import etree
html = etree.parse('hello.html')
result = etree.tostring(html, pretty_print=True)
print(result)



