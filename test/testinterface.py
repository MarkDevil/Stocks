# coding= utf-8
__author__ = '201512010283'

import requests
import unittest
from core.celerytask import *
import tushare as ts
from util.logutil import Log

params = {'mark1': 'val1', 'mark2': 'val2'}
data = {'version': '', 'bizCode': '', 'merchantCode': '', 'userId': ''}

log = Log('info').initlogger()


class mytest(unittest.TestCase):

    @unittest.skip("skip")
    def testGatewayParams(self):
        r = requests.get("http://localhost:5000/fgateway", params=params)
        print (r.url + '\t')

    def testcelerytask(self):
        checkTomcat.delay()

    def test_getcompany_profit(self):
        log.info(ts.get_profit_data(2018, 2))


if __name__ == '__main__':
    unittest.main()
