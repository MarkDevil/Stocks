# coding=utf-8
import re

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
    print time.ctime()
    for i in range(pages):
        url = 'http://bj.lianjia.com/ershoufang/pg' + str(i) + '/'
        page = urllib2.urlopen(url, timeout=50)
        soup = BeautifulSoup(page, "lxml")

        titles = soup.find_all('div', 'title')
        for m in titles:
            if (m.get_text() == '筛选：') or (m.get_text() == '用户登录还没有链家网账号？马上注册'):
                titles.remove(m)
                print 'delete invaid data :', m.get_text()
            else:
                continue
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
            rbuilding = fetchInfo(houseinfo=rhouseinfo, field='building')
            print rbuilding
            count += 1
            print("[count]- {} - [house]-[title]：{} - [houseinfo]:{} - [posinfo]:{} - [price]:{}"
                  .format(count, rtitle, rhouseinfo, rpos, rpriceInfo))
            # writedb(rtitle, rhouseinfo, rpos, rpriceInfo)
    print(time.ctime())


def writedb(title, houseinfo, posinfo, price):
    # INSERT INTO `lianjia`.`houseinfo` (`title`, `houseinfo`, `posinfo`, `price`) VALUES ('1', '1', '1', 1);
    insertsql = "REPLACE INTO lianjia.house (title, houseinfo, posinfo, price) VALUES ('%s', '%s', '%s', '%s');" % (
        title, houseinfo, posinfo, price)

    mysql.insertData(insertsql)


def fetchInfo(houseinfo, field):
    buildingreg = re.compile(r'^[\u4e00-\u9fa5]+').search(houseinfo)
    structreg = re.compile(r'\d[\u4e00-\u9fa5]\d[\u4e00-\u9fa5]').match(houseinfo)
    sizereg = re.compile(r'\d{3}.\d[\u4e00-\u9fa5]{2}').match(houseinfo)

    if field == 'building':
        return buildingreg.group(0)
    elif field == 'struct':
        return structreg
    elif field == 'size':
        return sizereg
    else:
        return None


if __name__ == '__main__':
    getlianjiadata(pages=100)