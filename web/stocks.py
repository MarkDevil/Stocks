# coding=utf-8
import os

from flask import Flask, request, session, redirect, url_for, flash, jsonify
from flask import json
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.checkTomcat import checkTomcatStatus
from core.form.nameform import NameForm
from core.stocks import Stocks
from mapper.role import Role
from util.configutil import ReadWriteConfFile
from util.emailutil import Sendmail

basedir = os.path.abspath(os.path.dirname(__file__))

stockapp = Flask(__name__)
stockapp.config['SECRET_KEY'] = 'mark'
stockapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
stockapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
bootstrap = Bootstrap(app=stockapp)
db = SQLAlchemy(stockapp)

maillist = [ReadWriteConfFile.getSectionValue('maillist', 'user')]
sendobj = Sendmail(mailto_list=maillist)
subjectTitle = '股票机构买入榜单'
profitTitle = '公司分红'

print(stockapp.config['SQLALCHEMY_DATABASE_URI'])
engine = create_engine('sqlite:///' + os.path.join(basedir, 'data.sqlite'))
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine, autocommit=True)


@stockapp.route('/fgateway', methods=["GET", "POST"])
def fgateway():
    a = request.get_json()
    js = json.dumps(a)
    return js


@stockapp.route('/getstocks')
def index():
    agentstocks = Stocks().findAgent()
    sendobj.send_mail(subjectTitle, str(agentstocks).decode("utf-8"))
    retmsg = str(agentstocks).decode("utf-8").format()
    return render_template('stockspage.html', retmsg=retmsg)


@stockapp.route('/user', methods={'GET', 'POST'})
def user():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('user'))
    return render_template('user.html',
                           form=form, name=session.get('name'))


@stockapp.route('/user/add/<name>', methods={'GET', 'POST'})
def add_user(name):
    admin_role = Role(name=name)
    # db.session.add(admin_role)
    session = DBSession()
    session.add(admin_role)
    ret = {'ret': 'ok'}
    return jsonify(ret)


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
    return render_template("404.html", err=e)


@stockapp.errorhandler(500)
def page_not_found(e):
    return render_template("500.html", err=e)


# @route('/gethouse', methods=["GET", "POST"])
# def gethouse():
#     mysql = Mysql()
#     dbsession = mysql.getSession()
#     list = dbsession.query(Lianjia).filter_by(region='回龙观').all()
#     return list


if __name__ == '__main__':
    stockapp.run(debug=True, threaded=True, port=1234)
