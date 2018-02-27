# coding=utf-8
__author__ = 'mingfengma'

from app.util.spyUtil import *


class spyHousePrice():

    def __init__(self, location=None, url=None, reg=None):
        self.location = location
        self.url = url
        self.reg = reg

    def getData(self):
        spyutils = SpyUtils()
        ret = spyutils.getcontent(url=self.url, reg=self.reg)
        print (ret)


if __name__ == '__main__':
    trendprice = r'<ul>.class=*+byzs*+'
    spyobj = spyHousePrice(location="回龙观", url="http://esf.fang.com/house-a012/a21/", reg=trendprice)
    spyobj.getData()
