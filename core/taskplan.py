# coding=utf-8

from celerytask import *


def checkjob():
    checkTomcat.delay()


if __name__ == '__main__':
    checkjob()
