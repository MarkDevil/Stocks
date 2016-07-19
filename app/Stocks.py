# coding=utf-8
from flask import Flask, request

from app.core.stocks import Stocks
from app.util.emailUtil import Sendmail


app = Flask(__name__)

sendobj = Sendmail("mamingfeng007@163.com")


@app.route('/fgateway', methods=["GET", "POST"])
def fgateway():
    var = request.get_data()
    print var
    return str(var)

@app.route('/getstocks')
def index():
    agentstocks = Stocks().findAgent()
    sendobj.send_mail("send email", str(agentstocks))
    return str(agentstocks).decode("utf-8")


if __name__ == '__main__':
    app.run(debug=True)
