# coding=utf-8
__author__ = '201512010283'
import tushare as ts


class Stocks:
    def __init__(self):
        pass

    '''
        机构净买入量最大的公司
    '''

    def findAgent(self):
        df = ts.inst_tops(10)
        df.sort_values(by='bamount')

        print df[df.net > 5000]
        return df[(df.net) > 5000]

    '''
        公司分红报告
    '''

    def getProfit(self, year=0, top=10, shares=10, divi=1):
        df = ts.profit_data(year=year, top=top)
        # df.sort('shares', ascending=False)
        print df.sort_values(by='divi', ascending=False)
        df1 = ts.inst_detail()
        print df1
        return df[df.divi >= divi]

    def getAgentStocks(self):
        pass

    def getlastedNews(self):
        return ts.get_latest_news(10, True)


if __name__ == '__main__':
    Stocks().findAgent()
