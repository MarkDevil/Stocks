# coding=utf-8
import re

import threading
from util.logutil import *
from util.spyutil import SpyUtils
from util.redisutil import RedisPool
import random
import time

logger = Log('info').initlogger()
spuy = SpyUtils()
redis = RedisPool().getRedis()



class ProxyPool(object):

    def __init__(self):
        pass




class ProxyGetter(object):

    threads = []

    def __init__(self):
        pass

    def checkUrls(self):
        start_url = 'https://www.kuaidaili.com/free/inha/1/'
        ret = spuy.get(start_url)
        logger.info(ret)

    def crawl_kuaidaili(self):
        logger.info('start crawl {}'.format('.....'))
        for page in range(1, 4, 1):
            # 国内高匿代理
            start_url = 'https://www.kuaidaili.com/free/inha/{}/'.format(page)
            logger.info(start_url)
            html = spuy.gethtml(start_url)
            logger.info('page source: ' + html)
            ip_adress = re.compile(
                '<td resource-title="IP">(.*)</td>\s*<td resource-title="PORT">(\w+)</td>'
            )
            re_ip_adress = ip_adress.findall(html)
            logger.info(re_ip_adress)
            for adress, port in re_ip_adress:
                # result = adress + ':' + port
                self.redis.set(adress, port)

    """
        yield 生成器函数，需要遍历返回值
    """

    def crawl_kuaidaili_old(self):
        # type: () -> object
        logger.info('start crawl {}'.format('.....'))
        page = random.choice(range(1, 100))
        # 国内高匿代理
        start_url = 'https://www.kuaidaili.com/free/inha/{}/'.format(page)
        logger.info("正在爬取第{}页数据".format(page))
        html = spuy.gethtml(start_url)
        ip_adress = re.compile(
            '<td resource-title="IP">(.*)</td>\s*<td resource-title="PORT">(\w+)</td>'
        )
        re_ip_adress = ip_adress.findall(html)
        for adress, port in re_ip_adress:
            result = adress + ':' + port
            logger.info(result)
            RedisPool().getRedis().hset('kuaidaili', adress, port)
            result.replace(' ', '')

    @classmethod
    def getproxy(cls):
        proxys = []
        dict = redis.hgetall('kuaidaili')
        for i in dict:
            proxys.append(str(i + ":" + str(dict[i])))
        proxy = random.choice(proxys)
        return proxy

    @classmethod
    def proxysNum(cls):
        dict = redis.hgetall('kuaidaili')
        logger.info("[http代理]代理池中的可用代理为[{}]".format(len(dict)))

    @classmethod
    def start(cls):
        threads = cls.threads
        for i in range(1, 10):
            threads.append(CrawlRun(i, "thread-{}".format(i)))
        for thread in threads:
            thread.start()
            time.sleep(2)
        for t in threads:
            t.join()


class CrawlRun(threading.Thread):

    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        logger.info("爬虫线程-{}-{} 启动成功".format(threadID, name))

    def run(self):
        p = ProxyGetter()
        p.crawl_kuaidaili_old()


if __name__ == '__main__':
    logger.info("获取到一个代理地址:{}".format(ProxyGetter.getproxy()))

    while True:
        ProxyGetter.proxysNum()
        ProxyGetter.start()
