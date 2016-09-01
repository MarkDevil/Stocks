# coding=utf-8
import MySQLdb
import logging
from configUtil import ReadWriteConfFile

__author__ = '201512010283'


def testMysql():
    db = MySQLdb.connect("10.100.141.39", "pay_trade", "pay_trade@123", "pay_trade")
    if db:
        print "create Database connection successfully"
        cursor = db.cursor()
        cursor.execute("SELECT * from pay_point.mall_order where merchant_code = 'MX_TOUMI'")
        data = cursor.fetchone()
        print str(data)
        db.close()
    else:
        print "create connection failed"


class Mysql():

    host = ReadWriteConfFile.getSectionValue('db', 'host')
    user = ReadWriteConfFile.getSectionValue('db', 'user')
    passwd = ReadWriteConfFile.getSectionValue('db', 'passwd')
    db = ReadWriteConfFile.getSectionValue('db', 'dbname')

    def __init__(self):
        pass
    @classmethod
    def getConn(cls):
        try:
            db = MySQLdb.connect(host=cls.host, user=cls.user, passwd=cls.passwd, db=cls.db,
                                 charset='utf8')
            return db
        except:
            print("create connection failed")


    def insertData(self, sql):
        db = self.getConn()
        cursor = db.cursor()
        try:
            cursor.execute(sql)
        except:
            print ("insert failed")
        finally:
            if db:
                db.close()


    def querydata(self, db, sql):
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        print ('data', isinstance(data, unicode))
        print "result number " + str(list(data))
        return data


    def printall(self, datas):
        print "Data number :" + str(len(datas))
        if len(datas) == 1:
            print datas
        else:
            for data in datas:
                print data


    def readsql(self, db, cursor):
        for line in open('src/sql/insertuser.sql', 'r'):
            formatline = line.strip()
            logging.info('execute sql : ' + formatline)
            try:
                cursor.execute(formatline)
                db.commit()
                logging.info("execute sql successfully")
            except:
                db.rollback()
                logging.info("execute sql failed")




if __name__ == '__main__':
    mysql = Mysql()
    datas = mysql.querydata(mysql.getConn(), "SELECT * from pay_financial.bank_account")
    logging.info(datas)



