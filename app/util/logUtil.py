__author__ = '201512010283'

import logging


def initlog():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s : %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='E:\\PycharmProjects\\Stocks\\app\\logs',
                        filemode='a')
    _logger1 = logging.getLogger("log")
    if _logger1:
        return _logger1
    else:
        return None


if __name__ == '__main__':
    initlog().log("info", "mark")
