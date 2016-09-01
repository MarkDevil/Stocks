# coding=utf-8
import MySQLdb
import logging
from configUtil import ReadWriteConfFile
import sqlalchemy

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

    '''
        插入数据如果主键冲突则打印信息
    '''
    def insertData(self, sql):
        db = self.getConn()
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
        except MySQLdb.IntegrityError:
            print 'data is duplicate'
        except Exception, e:
            db.rollback()
            raise e
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

    '''
        使用orm框架，创建数据库连接对象
    '''

    def getconn(self):
        dbconfig = {'host': self.host,
                    'user': self.user,
                    'passwd': self.passwd,
                    'db': 'test',
                    'charset': 'utf-8'
        }
        return sqlalchemy.create_engine('mysql://%s:%s@%s/%s?charset=%s'
                                        % (dbconfig['host'],
                                           dbconfig['user'],
                                           dbconfig['passwd'],
                                           dbconfig['db'],
                                           dbconfig['charset']
        ))


if __name__ == '__main__':
    mysql = Mysql()
    datas = mysql.querydata(mysql.getConn(), "SELECT * from pay_financial.bank_account")
    logging.info(datas)



