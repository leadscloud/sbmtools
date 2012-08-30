# -*- coding: utf-8 -*-

import re
import urllib
import urllib2
import BeautifulSoup

Filter = [' metso',' sandvik',' symons',' nordberg',' lokotrack',' trellex',' kefid',' liming',' break-day',' shanbao',' dsmac',' yifan',' hxjq',' 西蒙斯',' 美卓',' 山特维克',' 黎明',' 科菲达',' 山宝',' 建设路桥',' 鼎盛',' 一帆',' 红星']


userinput = raw_input("input URL:")

for fword in Filter:
    
    keyword = "site:" + urllib.quote_plus(userinput) + urllib.quote(fword)
    print keyword
    safeKeyword = urllib.quote_plus(keyword)
    fullQuery = 'http://www.baidu.com/s?ie=utf-8&wd=' + safeKeyword

    req = urllib2.Request(fullQuery, headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/12.04 Chrome/21.0.118083 Safari/535.11'})
    html = urllib2.urlopen(req).read()
    soup = BeautifulSoup.BeautifulSoup(html, fromEncoding = 'utf8')

#resultURLList = [t.contents[0].text for t in soup.findAll('div', {'class': 'f kv'})]
    resultURLList = [t.a['href'] for t in soup.findAll('h3', {'class':'t'})]


#print "#####---- Baidu ----####"

    if resultURLList:
        for l in resultURLList:
                print '%s : %s' % (fword.decode('utf-8').encode('gbk'), l)
    else:
        print '%s:  No Results' % fword.decode('utf-8').encode('gbk')

########



