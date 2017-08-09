__author__ = '201512010283'

import logging


class Log:
    def __init__(self, level):
        self.format = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s : %(message)s'
        self.datefmt = '%a, %d %b %Y %H:%M:%S'
        if level == "info":
            self.loglevel = logging.INFO
        elif level == "debug":
            self.loglevel = logging.DEBUG
        elif level == "warn":
            self.loglevel = logging.WARN
        else:
            self.loglevel = logging.INFO

    def initlogger(self):
        logging.basicConfig(
            level=self.loglevel,
            format=self.format,
            datefmt=self.datefmt,
        )
        return logging.getLogger()


if __name__ == '__main__':
    logger = Log("debug").initlogger()
    logger.info("mark test")
    logger.debug("mark test")
