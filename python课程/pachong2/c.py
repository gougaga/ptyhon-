from lxml import html

doc = """
<div>
    <ul class="item">
        <li class="item-0">
            <a href="link1.html">first item</a>
        </li>
        <li class="item-1">
            <a href="link2.html">second item</a>
        </li>
        <li class="item-inactive">
            <a href="link3.html">third item</a>
        </li>
        <li class="item-1">
            <a href="link4.html">fourth item</a>
        </li>
        <li class="item-0">
            <a href="link5.html">fifth item</a> 
        </li> 
    </ul>
 </div>
"""

page = html.etree.HTML(doc) #将响应结果转化为文档对象
# 获取所有的li标签
# li = page.xpath('/li')
# li = page.xpath('//ul/li')
# li = page.xpath('//div/ul/li')
# 获取所有a标签
a = page.xpath('//li/a')
# 获取a标签属性
shu = page.xpath('//li/a/@href')
# 获取a标签文字信息
wz = page.xpath('//li/a/text()')
# 获取最后一个a标签的文字信息
# la = page.xpath('//li/a/text()')
# print(type(la))
# print(la[-1])
# la = page.xpath('//li[last()-1]/a/text()')
# print(la)

# 获取所有li标签的class名
na = page.xpath('//li/@class')
print(na)

# 获取最class是 item-0 的li标签下的a标签的href属性
he = page.xpath('//li[@class = "item-0"]/a/@href')
print(he)

# 获取任意 class 是item 的 ul 标签下的 a标签href属性是link4.html的文字信息

cm = page.xpath('//ul[@class = "item"]//a[@href = "link4.html"]/text()')
print(cm)

sms = page.xpath('//*[contains(@class, "item")]')
print(len(sms))

xc = page.xpath('//*[starts-with(@href, "l")]')
print(len(xc))

# 前两个li标签下a标签的内容
# a = page.xpath('//ul/li[position() < 3]/a/text()')
a = page.xpath('//ul/li/a/text()')[:2]
print(a)