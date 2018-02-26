# coding=utf-8

from celerytask import sendmail,checkTomcat

def checkjob():
    checkTomcat.delay()


if __name__ == '__main__':
    checkjob()