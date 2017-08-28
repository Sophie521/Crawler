# -*- coding: utf-8 -*-
"""
Created on Wed Jan 04 17:23:04 2017

@author: PengZheng
"""

#import sys
#import os
#import numpy as np
#import pandas as pd
#import json

#import json

#w = open(r'E:\python\weather\weather.json')
#print w.read()

#pd.read_json('E:\python\weather\weather.json')

#from pandas.io.json import json_normalize
#!/usr/bin/env python
# 解释器路径
 
from HTMLParser import HTMLParser
import sys,urllib2,string,re
#导入使用方法模块
 
class HtmlParser(HTMLParser):
<span style="font-family: Arial, Verdana, sans-serif;">#定义一个类来完成这个功能</span>
 
    def __init__(self):
        self.data=''
        self.readingdata=0
        HTMLParser.__init__(self)
 
    def handle_starttag(self,tag,attrs):
        if tag == 'td':
            self.readingdata=1
 
    def handle_data(self,chars):
        if self.readingdata:
            self.data+=chars
 
    def handle_endtag(self,tag):
        if tag=='td':
            self.readingdata=0
 
    def cleanse(self):
        self.data = re.sub('\s+',' ', self.data)
 
    def getdata(self):
        self.cleanse()
        return self.data
 
# this url is a place where you want to know the weather forecast
url="http://www.weather.com.cn/html/weather/101210501.shtml"
 
req=urllib2.Request(url)
 
fd=urllib2.urlopen(req)
 
tp=HtmlParser()
 
tp.feed(fd.read())
 
weather=tp.getdata()
# when you are getting a weather after parsering
 
# this weather string have 7 days weather forecast
 
#www.iplaypython.com
 
# the following if for my awesome format
 
weather=weather.split()
 
tag=[weather.index(i) for i in weather if '\xe6\x97\xa5' in i]
first=weather[:tag[1]]
second=weather[tag[1]:tag[2]]
if second[1]!=second[7]:second[1]+=' --> '+second[7]
second[2]=second[9]+' --> '+second[3]
second[0]=second[0][:-6]
second=second[:3]
third=weather[tag[2]:tag[3]]
if third[1]!=third[7]:third[1]+=' --> '+third[7]
third[2]=third[9]+' --> '+third[3]
third[0]=third[0][:-6]
third=third[:3]
weather=['    Weather:']+first+['|']+second+['|']+third
 
for i in weather:print i,