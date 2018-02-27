# coding=utf-8
import re
from app.util.logUtil import *
from app.util.spyUtil import SpyUtils
from app.util.dbOperator import *
from app.Mapper.ipGetterMapper import IpInfo

logger = Log('info').initlogger()
spuy = SpyUtils()


class ProxyPool(object):

    def __init__(self):
        pass


class ProxyGetter(object):

    def __init__(self):
        self.session = mysql.getSession()

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
                '<td data-title="IP">(.*)</td>\s*<td data-title="PORT">(\w+)</td>'
            )
            re_ip_adress = ip_adress.findall(html)
            logger.info(re_ip_adress)
            for adress, port in re_ip_adress:
                # result = adress + ':' + port
                session.add(IpInfo(adress, port))
        session.commit()
        session.close()

    def crawl_kuaidaili_old(self):
        # type: () -> object
        print('start crawl {}'.format('.....'))
        for page in range(1, 4):
            # 国内高匿代理
            start_url = 'https://www.kuaidaili.com/free/inha/{}/'.format(page)
            logger.info(start_url)
            html = spuy.gethtml(start_url)
            ip_adress = re.compile(
                '<td data-title="IP">(.*)</td>\s*<td data-title="PORT">(\w+)</td>'
            )
            re_ip_adress = ip_adress.findall(html)
            for adress, port in re_ip_adress:
                result = adress + ':' + port
                logger.info(result)
                yield result.replace(' ', '')


if __name__ == '__main__':
    # ProxyGetter().checkUrls()
    ProxyGetter().crawl_kuaidaili()
