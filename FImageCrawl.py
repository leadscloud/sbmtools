#coding=utf-8

import re
import urllib, urllib2
import thread
import time
import os

url_part1 = '''http://www.flickr.com/search/?q='''
url_part2 = '''&m=tags'''
url_part3 = '''&page='''

#  http://www.flickr.com/search/?q=vista&m=tags&page=2

def nextpage(keywords,start):
    return url_part1 + urllib.quote(keywords) + url_part2 + url_part3+str(start)

compile_obj = re.compile(r'dyn.Img\(".*?",".*?",".*?","(.*?)"')


def parseurl(content):
    ret = []
    match_objs = compile_obj.findall(content)
    for url in match_objs:
        ret.append(url)
        print url
    return ret

#exitdic = {}

def downimg(url,exitdic):
    filename = url.split('/')[-1]
    print url,'---->',filename
    urllib.urlretrieve(url,filename)
    print filename
    exitdic[url].acquire()

def download(url):
    exitdic = {}
    print '开始下载页面: ' + url
    conn = urllib2.Request(url)
    conn.add_header('User-Agent', 'Firefox/15 Linux i386')
    opener = urllib2.build_opener()
    content = opener.open(conn).read()
    urls = parseurl(content)
    for url in urls:
        exitdic[url] = thread.allocate_lock()
        thread.start_new(downimg,(url,exitdic))
    
    for key in exitdic.keys():
        while not exitdic[key].locked():
            time.sleep(200)
            pass
    print 'Done'

if __name__ == '__main__':
    for i in range(1,3):
        keyword='london'
        directory='c:/temp_flikr/'+keyword
        if not os.path.exists(directory):
            os.makedirs(directory)
        os.chdir(directory)
        url = nextpage(keyword,i)
        download(url)
    
    print 'OK'
