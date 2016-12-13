# coding=utf-8
__author__ = 'mingfengma'

from app.util.spyUtil import *


spyutil = SpyUtils()


def getSSpasswd(url):
    if url is not None:
        retlist = SpyUtils.getcontent(spyutil, '.服务器地址:\w.\w+.\w+', url)
        portlist = SpyUtils.getcontent(spyutil, '端口:\d+', url)
        passwdlist = SpyUtils.getcontent(spyutil, '.密码.\d+', url)

        for num in range(len(retlist)):
            print str.format(" Server '%s'" % (num))
            print str.format(" server addr :%s \n port number : '%s' \n passwd :'%s'"
                             % (retlist[num], portlist[num], passwdlist[num]))
            f = file("sspaswd.txt", "a+")
            cont = [retlist[num], '\t', portlist[num], '\t', passwdlist[num]]
            f.writelines(cont)
            f.writelines("\n")
        f.close()
        return


if __name__ == '__main__':
    getSSpasswd("https://www.ishadowsocks.biz/#free")