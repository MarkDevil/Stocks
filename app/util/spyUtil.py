# coding=utf-8
__author__ = 'mingfengma'

import re
import urllib2
import json
from BeautifulSoup import BeautifulSoup
import zlib


class SpyUtils:
    '''
        http://esf.fang.com/house-a012-b01182/
        查询网站
    '''

    def __init__(self):
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
        self.header = {"User-Agent": user_agent}

    def requestheader(self):
        return self.header

    '''
        返回符合模式的数据
    '''

    def getcontent(self, reg, url):
        return re.findall(reg, self.gethtml(url=url))

    def gethtml(self, url):
        request = urllib2.Request(url=url, headers=self.requestheader())
        request.add_header('Accept-encoding', 'gzip')
        response = urllib2.urlopen(request)
        html = response.read()
        gzipped = response.headers.get('Content-Encoding')
        if gzipped:
            html = zlib.decompress(html, 16 + zlib.MAX_WBITS)
            return html
        else:
            return html

    '''
    获取指定页面数据
    '''

    def getelements(self, url, nodename, attrs=None, title=None, text=None):
        soup = BeautifulSoup(self.gethtml(url))
        pricetrend = soup.findAll(nodename, attrs=attrs, title=title, text=text)
        for i in pricetrend:
            print i
        return pricetrend


    def cleanstr(self, str, partten):
        reg = re.search(partten, str)
        if reg:
            return reg.group()
        else:
            return None


if __name__ == '__main__':
    numParten = r'\d+.\d+'
    rest = SpyUtils().getelements("http://esf.fang.com/house-a012-b01182")
    print SpyUtils().cleanstr(str(rest), numParten)



