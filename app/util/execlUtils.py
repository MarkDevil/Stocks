# coding=utf-8

import pandas as panda
from logUtil import Log

LOGDEBUG = Log("debug").initlogger()
LOGINFO = Log("info").initlogger()


class ExcelUtils:

    def __init__(self):
        pass

    def gendata(self, colname, rowdata):
        retmap = map(None, colname, rowdata)
        print  dict(retmap)

    @staticmethod
    def readexcel(filename, sheetname):
        if filename is not None:
            df = panda.read_excel(filename, sheetname=sheetname, na_values=['NA'])
            lenr = df.__len__()
            hnames = df.keys()
            print hnames
            for i in range(0, lenr):
                rowdata = df.ix[i]
                print type(rowdata)
                excelutl = ExcelUtils()
                excelutl.gendata(hnames, rowdata)


if __name__ == '__main__':
    ExcelUtils.readexcel('/Users/mark/Desktop/随手记贷后需求/随手记测算表-20171212终稿.xlsx', sheetname='test2')
