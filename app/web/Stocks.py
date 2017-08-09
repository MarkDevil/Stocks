# coding=utf-8
from flask import Flask, request
from flask import json
from flask import render_template

from app.core.stocks import Stocks
from app.util.configUtil import ReadWriteConfFile
from app.util.emailUtil import Sendmail

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
    # sendobj.send_mail(subjectTitle, str(agentstocks).decode("utf-8"))
    # return str(agentstocks).decode("utf-8").format()
    ret_msg = str(agentstocks).decode("utf-8").format()
    return render_template('StocksPage.html', ret_msg=ret_msg)


# @app.route('/gethouse', methods=["GET", "POST"])
# def gethouse():
#     mysql = Mysql()
#     dbsession = mysql.getSession()
#     list = dbsession.query(Lianjia).filter_by(region='回龙观').all()
#     return list


if __name__ == '__main__':
    app.run(debug=True)
