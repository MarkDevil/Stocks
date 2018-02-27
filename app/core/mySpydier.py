# coding=utf-8
__author__ = 'mingfengma'
from bs4 import BeautifulSoup
import socket
import urllib2
import re
import zlib


class MyCrawler:
    def __init__(self, seeds):

        self.current_deepth = 1
        self.linkQuence = linkQuence()
        if isinstance(seeds, str):
            self.linkQuence.addUnvistedUrl(seeds)
            print("Data enter in queue : " + seeds)
        if isinstance(seeds, list):
            for i in seeds:
                self.linkQuence.addUnvistedUrl(i)
                # print "Add the seeds url \"{0:s}\" to the unvisited url list".format

    def crawling(self, seeds, crawl_depth):
        while self.current_deepth <= crawl_depth:
            while not self.linkQuence.unVistedUrlsIsempty():
                vistUrl = self.linkQuence.unVistedUrlDeQueue()
                print ("Pop out one url \"%s\" from unvisited url list" % vistUrl)
                if vistUrl is None or vistUrl == "":
                    continue

                links = self.getHyperLinks(vistUrl)
                print ("Get %d new links" % len(links))

                self.linkQuence.addVistedUrl(vistUrl)
                print ("Visited url count: " + str(self.linkQuence.getVistedUrlCount()))
                print ("Visited deepth: " + str(self.current_deepth))

            for link in links:
                self.linkQuence.addUnvistedUrl(link)
            print ("%d unvisited links:" % len(self.linkQuence.getUnVistedUrl()))
            self.current_deepth += 1

    '''
        获取页面的链接
    '''

    def getHyperLinks(self, url):
        links = []
        data = self.getPageSource(url)
        if data[0] == "200":
            soup = BeautifulSoup(data[1], 'lxml')
            a = soup.findAll(href=re.compile("^http"))
            print (soup.prettify(formatter="html"))
            # print a
            for i in a:
                if i["href"].find("http://") != -1:
                    print("found url : ", i["href"])
                    links.append(i["href"])
        return links

    '''
        获取页面的源码
    '''
    def getPageSource(self, url, timeout=100):

        socket.setdefaulttimeout(timeout)
        req = urllib2.Request(url)
        req.add_header('User-agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')
        response = urllib2.urlopen(req)
        # print response
        page = ''
        if response.headers.get('Content-Encoding') == 'gzip':
            page = zlib.decompress(page, 16 + zlib.MAX_WBITS)
        else:
            page = response.read()
            # page = page.decode(coding).encode('utf-8')
        return ["200", page]



class linkQuence:
    def __init__(self):
        self.visted = []
        self.unVisted = []

    def getVistedUrl(self):
        return self.visted

    def getUnVistedUrl(self):
        return self.unVisted

    def addVistedUrl(self, url):
        return self.visted.append(url)

    def removeVistedUrl(self, url):
        return self.unVisted.remove(url)

    def unVistedUrlDeQueue(self):
        try:
            return self.unVisted.pop()
        except:
            return None

    def addUnvistedUrl(self, url):
        if url != "" and url not in self.visted and url not in self.unVisted:
            self.unVisted.insert(0, url)

    def getVistedUrlCount(self):
        return self.visted.__len__()

    def getUnVistedUrlCount(self):
        return self.unVisted.__len__()

    def unVistedUrlsIsempty(self):
        return len(self.unVisted) == 0


def main(seeds, crawl_deepth):
    craw = MyCrawler(seeds)
    craw.crawling(seeds, crawl_deepth)


if __name__ == '__main__':
    main(["http://www.baidu.com"], 10)




