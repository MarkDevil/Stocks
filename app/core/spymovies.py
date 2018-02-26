# coding = utf-8

from app.util.spyUtil import *

spy = SpyUtils()


def getmovieinfo():
    elems = spy.getelements(url='https://movie.douban.com/', nodename='a')
    for ele in elems:
        print(ele)


if __name__ == '__main__':
    getmovieinfo()
