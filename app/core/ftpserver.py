from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import MultiprocessFTPServer, ThreadedFTPServer  # <-
from pyftpdlib.authorizers import DummyAuthorizer

import app.util.logUtil

server = None

logger = app.util.logUtil.Log("info").initlogger()


def startftpServer(concurrytype):
    global server
    authorizer = DummyAuthorizer()
    authorizer.add_user('user', '12345', '.')
    handler = FTPHandler
    handler.authorizer = authorizer
    if concurrytype == 'process':
        server = MultiprocessFTPServer(('', 2121), handler)
    elif concurrytype == 'thread':
        server = ThreadedFTPServer(('', 2121), handler)
    else:
        logger.info('Enter type mismatch')
    server.serve_forever()


if __name__ == "__main__":
    startftpServer(concurrytype='thread')
