# coding=utf-8
from flask import Flask, request
from app.core import spyLianjia

from app.core.stocks import Stocks
from app.util.emailUtil import Sendmail
from app.util.configUtil import ReadWriteConfFile
from app.util.dbOperator import Mysql
from app.Mapper.lianjiaMapper import *
from flask import json


app = Flask(__name__)

maillist = [ReadWriteConfFile.getSectionValue('maillist', 'user')]
sendobj = Sendmail(mailto_list=maillist)
subjectTitle = '股票机构买入榜单'


@app.route('/fgateway', methods=["GET", "POST"])
def fgateway():
    a = request.get_json()
    print a
    js = json.dumps(a)
    return js


@app.route('/getstocks')
def index():
    agentstocks = Stocks().findAgent()
    sendobj.send_mail(subjectTitle, str(agentstocks).decode("utf-8"))
    return str(agentstocks).decode("utf-8").format()


@app.route('/gethouse', methods=["GET", "POST"])
def gethouse():
    mysql = Mysql()
    dbsession = mysql.getSession()
    list = dbsession.query(Lianjia).filter_by(region='回龙观').all()
    return list


if __name__ == '__main__':
    app.run(debug=True)
