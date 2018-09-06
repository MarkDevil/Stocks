# coding=utf-8
import smtplib
from email.mime.text import MIMEText

from util.configutil import ReadWriteConfFile

__author__ = '201512010283'


class Sendmail():
    def __init__(self, mailto_list):
        self.mailto_list = mailto_list
        self.mail_host = "smtp.163.com"  # 设置服务器
        self.mail_user = "mamingfeng007"  # 用户名
        self.mail_pass = "crystal08"  # 口令
        self.mail_postfix = "163.com"  # 发件箱的后缀

    def send_mail(self, sub, content):
        me = "hello" + "<" + self.mail_user + "@" + self.mail_postfix + ">"
        msg = MIMEText(content, _subtype='plain', _charset='gb2312')
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ";".join(self.mailto_list)

        server = smtplib.SMTP()
        server.connect(self.mail_host)
        server.login(self.mail_user, self.mail_pass)
        server.sendmail(me, self.mailto_list, msg.as_string())
        server.close()


if __name__ == '__main__':

    mailto_list = [str(ReadWriteConfFile.getSectionValue("maillist", "user"))]
    sendobj = Sendmail(mailto_list)
    if sendobj.send_mail("hello", "hello world python test"):
        print ("发送成功")
    else:
        print ("发送失败")
