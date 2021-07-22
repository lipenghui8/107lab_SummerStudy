# import lxml.html,requests
# url='https://www.python.org/dev/peps/pep-0020/'
# xpath='//*[@id="the-zen-of-python"]/pre/text()'
# res=requests.get(url)
# ht=lxml.html.fromstring(res.text)
# text=ht.xpath(xpath)
# print('hello,\n'+''.join(text))
# import urllib.robotparser as urobot
# import requests
# url="https://www.taobao.com/"
# rp=urobot.RobotFileParser()
# rp.set_url(url+'robots.txt')
# rp.read()
# user_agent='aa'
# if rp.can_fetch(user_agent,'https://www.taoba.com/product/'):
#     site=requests.get(url)
#     print('seem good')
# else:
#     print("cannot scrap because robots.txt banned you!")
# import wad.detection
# det=wad.detection.Detector()
# url="https://www.12306.cn/"
# print(det.detect(url))
# import bs4,requests,re
# from bs4 import BeautifulSoup
# ht=requests.get('https://www.qimao.com/')
# bs1=BeautifulSoup(ht.content)
# print(bs1.prettify())
# print("title")
# print(bs1.title)
# print('title.name')
# print(bs1.title.name)
# print('title.parent.name')
# print(bs1.title.parent.name)
# print('find all "a"')
# print(bs1.find_all('a'))
# print('text of all "h2"')
# for one in bs1.find_all('h2'):
#     print(one.text)
# print(bs1.find_all('clearfix'))
from lxml import html
import requests
text=requests.get('https://www.bilibili.com').text
ht=html.fromstring(text)
h1Ele=ht.xpath('//*[@class="info-box"]')[0]
print(h1Ele.text)
print(h1Ele.attrib)
print(h1Ele.get('class'))
print(h1Ele.keys())
print(h1Ele.values())
