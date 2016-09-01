# coding=utf-8
__author__ = 'mingfengma'

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

import urllib2
import time
from bs4 import BeautifulSoup
from app.util.dbOperator import Mysql


mysql = Mysql()
conn = Mysql.getConn()

def getlianjiadata(pages):
    count = 0
    print time.gmtime()
    for i in range(pages):
        url = 'http://bj.lianjia.com/ershoufang/pg' + str(i) + '/'
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, "lxml")

        titles = soup.find_all('div', 'title')
        houseInfos = soup.find_all('div', 'houseInfo')
        positionInfos = soup.find_all('div', 'positionInfo')
        followInfos = soup.find_all('div', 'followInfo')
        tagInfos = soup.find_all('div', 'tag')
        priceInfos = soup.find_all('div', 'totalPrice')
        for title, houseinfo, pos, priceInfo in zip(titles, houseInfos, positionInfos, priceInfos):
            rtitle = title.get_text()
            rhouseinfo = houseinfo.get_text()
            rpos = pos.get_text()
            rpriceInfo = priceInfo.get_text()
            count += 1
            print("[count]- {} - [house]-[title]：{} - [houseinfo]:{} - [posinfo]:{} - [price]:{}"
                  .format(count, rtitle, rhouseinfo, rpos, rpriceInfo))
    print(time.gmtime())


def writedb():
    insertsql = "insert into db values () "
    mysql.insertData()



if __name__ == '__main__':
    getlianjiadata(1000)