# coding=utf-8
from app.util.spyUtil import SpyUtils
import re
from threading import Timer


__author__ = 'mingfengma'


class SpyPeopleWeb():
    def __init__(self):
        pass

    def parseUrl(self):
        spy = SpyUtils()
        retlist = spy.getelements(url="http://www.bjcyrc.gov.cn/tzgg/",
                                  nodename='a',
                                  title=re.compile(r'[\u4e00-\u9fa5]+')
        )

        for ret in retlist:
            print("Get data from 'www.bjcyrc.gov.cn' :", ret)
            # self.cleanData(str(ret), r'[^[.[\u4e00-\u9fa5]+.]]')
            # return len(retlist)

    def cleanData(self, content, pattern):
        strinfo = re.sub(pattern=pattern, string=content, repl="")
        print ("After clean string ", strinfo)



    def start(self):
        mytimer = Timer(2.0, SpyPeopleWeb().parseUrl)
        mytimer.start()


if __name__ == '__main__':

    SpyPeopleWeb().start()
