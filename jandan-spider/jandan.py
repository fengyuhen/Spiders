# coding=utf-8

import urllib
import urllib2
from lxml import etree
import random

class Spdier:
    def __init__(self):
        self.siteURL = "http://www.jandan.net/drawings/"
        self.agentSet = []
        self.agentSet.append("Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19")
        self.agentSet.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36")
        # self.agentSet.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36")


    # the function return html
    def getPages(self, pageIndex):
        url = self.siteURL + "page-" + str(pageIndex) + "#cpmments"
        print(url)

        #header
        rand = random.randint(0,1)
        User_Agent = self.agentSet[rand]
        headers = {'User-Agent': User_Agent}
        #post a request
        try:
            request = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(request)
        except urllib2.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
        return response.read()


    def saveImg(self, imageURL, filename):
        print(filename)
        if(filename[-3:] == 'jpg'):
            u = urllib.urlopen(imageURL)
            data = u.read()
            f = open(filename, 'wb')
            f.write(data)
            f.close()
        elif(filename[-3:] == 'gif'):
            pass

    def getContents(self, pageIndex):
        html = self.getPages(pageIndex)
        selector = etree.HTML(html)
        print(selector)
        items = selector.xpath('//*[@id="comments"]/ol/li/div/div/div[2]/p[2]/img/@src')
        j = 0
        for item in items:
            print(item)
            self.saveImg(item, str(pageIndex) + '-' + str(j) + item[-4:])
            j += 1

m = 10
spider = Spdier()
for i in xrange(21, 22):
    print(i)
    spider.getContents(i)
    pass