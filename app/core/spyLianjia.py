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
from app.util.Workers import Worker, WorkManager

mysql = Mysql()
conn = Mysql.getConn()
wm = WorkManager()


def getlianjiadata(pages):
    count = 0
    print (time.ctime())
    for i in range(0, pages):
        url = 'http://bj.lianjia.com/ershoufang/pg' + str(i) + '/'
        print ('starting parse page : ', str(i))
        page = urllib2.urlopen(url, timeout=50)
        soup = BeautifulSoup(page, "lxml")

        titles = soup.find_all('div', 'title')
        for m in titles:
            if (m.get_text() == '筛选：') or (m.get_text() == '用户登录还没有链家网账号？马上注册'):
                titles.remove(m)
                print ('delete invaild data :', m.get_text())
            else:
                continue
        houseInfos = soup.find_all('div', 'houseInfo')
        positionInfos = soup.find_all('div', 'positionInfo')
        # followInfos = soup.find_all('div', 'followInfo')
        # tagInfos = soup.find_all('div', 'tag')
        priceInfos = soup.find_all('div', 'totalPrice')
        for title, houseinfo, pos, priceInfo in zip(titles, houseInfos, positionInfos, priceInfos):
            rtitle = title.get_text()
            rurl = fetchInfo(info=str(houseinfo), field='url')
            rhouseinfo = houseinfo.get_text()
            rpos = pos.get_text()
            rregion = fetchInfo(info=rpos, field='region')
            ryear = fetchInfo(info=rpos, field='year')
            rfloor = fetchInfo(info=rpos, field='floor')
            rpriceInfo = priceInfo.get_text()
            rbuilding = fetchInfo(info=rhouseinfo, field='building')
            rstruct = fetchInfo(info=rhouseinfo, field='struct')
            rsize = fetchInfo(info=rhouseinfo, field='size')
            count += 1
            print("[count]- {} - [house]-[title]：{} - [houseinfo]:{} - [posinfo]:{} - [price]:{} - {}"
                  .format(count, rtitle, rhouseinfo, rpos, rpriceInfo, rurl))
            writedb(rtitle, rhouseinfo, rbuilding, rstruct, rsize, rpos, rpriceInfo, rregion, ryear, rfloor, rurl)

    print(time.ctime())


def writedb(title, houseinfo, building, struct, size, posinfo, price, region, syear, floor, url):
    insertsql = "REPLACE INTO lianjia.house " \
                "(title, houseinfo, posinfo,building, struct, housesize, price,region,syear,floor, url_addr) " \
                "VALUES ('%s', '%s', '%s','%s','%s','%s', '%s', '%s', '%s', '%s' ,'%s');" \
                % (title, houseinfo, posinfo, building, struct, size, price, region, syear, floor, url)
    mysql.insertData(insertsql)


def fetchInfo(info, field):
    if info is None or field is None:
        raise Exception('input message is none')
    if field == 'building':
        return re.compile(r' | ').split(info).__getitem__(0)
    elif field == 'struct':
        return re.compile(r' | ').split(info).__getitem__(2)
    elif field == 'size':
        return re.compile(r' | ').split(info).__getitem__(4)
    elif field == 'url':
        return re.findall(r"http.+\d+/", info).__getitem__(0)
    elif field == 'floor':
        return re.compile(r' ').split(info).__getitem__(0)
    elif field == 'year':
        return re.compile(r' ').split(info).__getitem__(2)
    elif field == 'region':
        return re.compile(r' ').split(info).__getitem__(6)
    else:
        return None


if __name__ == '__main__':
    getlianjiadata(pages=200)
