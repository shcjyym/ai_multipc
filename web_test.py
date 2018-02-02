# -*- coding: UTF-8 -*-
import urllib
import re


def getHTML(url):
    response = urllib.urlopen(url)
    html = response.read()
    return html


def getImg(html):
    reg = 'src="(.+?\.jpg)"'
    img = re.compile(reg)
    html = html.decode('utf-8')
    imglist = re.findall(img, html)
    print imglist
    x = 0
    for i in range(20):
        imgurl = imglist[i]
        print imgurl
        urllib.urlretrieve(imgurl, 'D:/Scratch/%s.jpg' % x)
        x += 1


global Max_Num
Max_Num = 1
for i in range(Max_Num):
    try:
        html = getHTML("http://blog.csdn.net/Huilaojia123/article/details/53926792")
        print html
        getImg(html)
        break
    except:
        if i < Max_Num - 1:
            continue
        else:
            print ('URLError: <urlopen error timed out> All times is failed ')
