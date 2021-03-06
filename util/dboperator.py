# coding=utf-8
import MySQLdb
import logging
from mapper.lianjiaMapper import *
from configutil import ReadWriteConfFile
import sqlalchemy
from sqlalchemy.orm import sessionmaker

__author__ = 'mark'


def testMysql():
    db = MySQLdb.connect("localhost")
    if db:
        print ("init Database connection successfully")
        cursor = db.cursor()
        cursor.execute("SELECT * from pay_point.mall_order where merchant_code = 'MX_TOUMI'")
        data = cursor.fetchone()
        print (str(data))
        db.close()
    else:
        print ("create connection failed")


class Mysql:
    host = ReadWriteConfFile.getSectionValue('db', 'host')
    user = ReadWriteConfFile.getSectionValue('db', 'user')
    passwd = ReadWriteConfFile.getSectionValue('db', 'passwd')
    db = ReadWriteConfFile.getSectionValue('db', 'dbname')

    def __init__(self):
        # type: () -> object
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
            print ('resource is duplicate')
        finally:
            if db:
                db.close()

    def querydata(self, db, sql):
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        print ('resource', isinstance(data, unicode))
        print ("result number " + str(list(data)))
        return data

    def printall(self, datas):
        print ("Data number :" + str(len(datas)))
        if len(datas) == 1:
            print (datas)
        else:
            for data in datas:
                print (data)

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

    def getEngine(self):
        dbconfig = {'host': self.host,
                    'user': self.user,
                    'passwd': self.passwd,
                    'db': self.db,
                    'charset': 'utf8'
                    }
        return sqlalchemy.create_engine('mysql+mysqldb://%s:%s@%s/%s?charset=%s'
                                        % (dbconfig['user'],
                                           dbconfig['passwd'],
                                           dbconfig['host'],
                                           dbconfig['db'],
                                           dbconfig['charset']
                                           ))

    '''
        返回数据库会话
    '''

    def getSession(self):
        DBsession = sessionmaker(bind=self.getEngine())
        session = DBsession()
        return session

    def findall(self, clsname, **kwargs):
        if clsname is None or kwargs is None:
            raise Exception('Search parameter is incorrect !')
        session = self.getSession()
        retlist = session.query(clsname).filter_by(**kwargs).all()
        self.printlist(retlist)
        return retlist

    def printlist(self, inlist):
        for i in inlist:
            for key, value in i.__dict__.items():
                print (key, value)


if __name__ == '__main__':
    mysql = Mysql()
    session = mysql.getSession()
    # tuser = User(id='1', title='马铭锋')
    # session.add(tuser)
    # session.commit()
    lianjia = session.query(Lianjia).filter_by(region='回龙观').all()
    for i in lianjia:
        for key, value in i.__dict__.items():
            print (key, value)
        print ('\n')
    mysql.findall(Lianjia, region='霍营')
