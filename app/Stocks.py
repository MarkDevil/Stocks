# coding=utf-8
from flask import Flask, request

from app.core.stocks import Stocks
from app.util.emailUtil import Sendmail
from app.util.configUtil import ReadWriteConfFile
import time


app = Flask(__name__)

maillist = [ReadWriteConfFile.getSectionValue('maillist', 'user')]
sendobj = Sendmail(mailto_list=maillist)
subjectTitle = '股票机构买入榜单'


@app.route('/fgateway', methods=["GET", "POST"])
def fgateway():
    var = request.get_data()
    print str(var)
    return str(var)


@app.route('/getstocks')
def index():
    agentstocks = Stocks().findAgent()
    sendobj.send_mail(subjectTitle, str(agentstocks).decode("utf-8"))
    return str(agentstocks).decode("utf-8")

@app.route('/gethouse', methods=["GET", "POST"])
def gethouse():
    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
