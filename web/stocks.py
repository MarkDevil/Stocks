# coding=utf-8
from flask import Flask, request
from flask import json
from flask import render_template
import os

from core.stocks import Stocks
from util.configutil import ReadWriteConfFile
from util.emailutil import Sendmail
from core.checkTomcat import checkTomcatStatus


stockapp = Flask(__name__)

maillist = [ReadWriteConfFile.getSectionValue('maillist', 'user')]
sendobj = Sendmail(mailto_list=maillist)
subjectTitle = '股票机构买入榜单'
profitTitle = '公司分红'


@stockapp.route('/fgateway', methods=["GET", "POST"])
def fgateway():
    a = request.get_json()
    js = json.dumps(a)
    return js


@stockapp.route('/getstocks')
def index():
    agentstocks = Stocks().findAgent()
    sendobj.send_mail(subjectTitle, str(agentstocks).decode("utf-8"))
    # profitStocks = Stocks().getProfit(2016)
    # return str(agentstocks).decode("utf-8").format()
    # sendobj.send_mail(subjectTitle, str(agentstocks).decode("utf-8"))
    # return str(agentstocks).decode("utf-8").format()
    ret_msg = str(agentstocks).decode("utf-8").format()
    return render_template('StocksPage.html', ret_msg=ret_msg)


@stockapp.route('/getNews', methods=["GET"])
def getnews():
    news = Stocks().getlastedNews()
    print (news)
    retmsg = str(news).decode("utf-8").format()
    return render_template("main.html", retmsg=retmsg)


@stockapp.route('/getStats', methods=["GET"])
def getStats():
    fd = checkTomcatStatus()
    # retmsg = json.dumps(fd)
    print (type(fd))
    return render_template("main.html", retmsg=fd)


@stockapp.errorhandler(404)
def page_not_found(e):
    return "page not found"


# @route('/gethouse', methods=["GET", "POST"])
# def gethouse():
#     mysql = Mysql()
#     dbsession = mysql.getSession()
#     list = dbsession.query(Lianjia).filter_by(region='回龙观').all()
#     return list


if __name__ == '__main__':
    stockapp.run(debug=True, threaded=True)
