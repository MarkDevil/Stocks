# coding=utf-8
import logging

import requests
from util.spyutil import *


class SpyCar:
    '''
        https://otc.cbex.com/page/jpxkc/s/index
    '''

    def __init__(self, url):
        logging.captureWarnings(True)
        self.url = url

    def get_web_source(self):
        rets = SpyUtils().getelements(self.url, 'div', {'id': 'container'})
        for ret in rets:
            ret.findAll('div', {'class': 'zclist'})
        print(ret)


    # def check_car_auction(self):


if __name__ == '__main__':
    SpyCar('https://otc.cbex.com/page/jpxkc/s/index').get_web_source()
