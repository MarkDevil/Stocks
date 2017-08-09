# coding=utf-8
__author__ = '201512010283'
import os
import tushare as ts


class Stocks:
    def __init__(self):
        pass

    def findAgent(self):
        df = ts.inst_tops(10)
        df.sort_values(by='bcount')

        print df[(df.net) > 5000]
        return df[(df.net) > 5000]


    # 获取分红信息
    def getProfit(self, year, top, shares=0, divi=0):
        df = ts.profit_data(year=year, top=top)
        # df.sort('shares', ascending=False)
        df.sort_values(by='divi')
        return df[df.divi >= divi]

    def getAgentStocks(self):
        pass


if __name__ == '__main__':
    Stocks().findAgent()
