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
        # followInfos = soup.find_all('div', 'followInfo')
        # tagInfos = soup.find_all('div', 'tag')
        priceInfos = soup.find_all('div', 'totalPrice')
        for title, houseinfo, pos, priceInfo in zip(titles, houseInfos, positionInfos, priceInfos):
            rtitle = title.get_text()
            rurl = fetchInfo(houseinfo=str(houseinfo), field='url')
            rhouseinfo = houseinfo.get_text()
            rpos = pos.get_text()
            rpriceInfo = priceInfo.get_text()
            rbuilding = fetchInfo(houseinfo=rhouseinfo, field='building')
            rstruct = fetchInfo(houseinfo=rhouseinfo, field='struct')
            rsize = fetchInfo(houseinfo=rhouseinfo, field='size')
            count += 1
            print("[count]- {} - [house]-[title]：{} - [houseinfo]:{} - [posinfo]:{} - [price]:{} - {}"
                  .format(count, rtitle, rhouseinfo, rpos, rpriceInfo, rurl))
            writedb(rtitle, rhouseinfo, rbuilding, rstruct, rsize, rpos, rpriceInfo, rurl)
    print(time.ctime())


def writedb(title, houseinfo, building, struct, size, posinfo, price, url):
    insertsql = "REPLACE INTO lianjia.house " \
                "(title, houseinfo, posinfo,building, struct, housesize, price, url_addr) " \
                "VALUES ('%s', '%s', '%s','%s','%s','%s', '%s', '%s');" % (
                    title, houseinfo, posinfo, building, struct, size, price, url)
    mysql.insertData(insertsql)


def fetchInfo(houseinfo, field):
    if houseinfo is None or field is None:
        raise Exception('input message is none')

    if field == 'building':
        buildingreg = re.compile(r' | ').split(houseinfo).__getitem__(0)
        return buildingreg
    elif field == 'struct':
        structreg = re.compile(r' | ').split(houseinfo).__getitem__(2)
        return structreg
    elif field == 'size':
        sizereg = re.compile(r' | ').split(houseinfo).__getitem__(4)
        return sizereg
    elif field == 'url':
        urlreg = re.findall(r"http.+\d+/", houseinfo).__getitem__(0)
        return urlreg
    else:
        return None


if __name__ == '__main__':
    getlianjiadata(pages=100)