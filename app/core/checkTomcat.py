__author__ = 'mingfengma'

import paramiko
import app.util.logUtil

HOSTS = ['192.168.18.45']
PORT = 22
USER = 'root'
PASSWD = 'qwe123ASD()'
logger = app.util.logUtil.Log("info").initlogger()


def checkTomcatStatus():
    fd = {}
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for host in HOSTS:
        ssh.connect(host, PORT, USER, PASSWD)
        stdin, stdout, stderr = ssh.exec_command('ps -ef | grep hbadmin | grep -v grep | awk \'{print $2}\'')
        data = stdout.read()
        pid = data
        logger.info("PID number is " + pid)
        if data is not None:
            fd[host] = 'ok'
        else:
            fd[host] = 'bad'
    ssh.close()
    logger.info("Check status is '%s'", fd)
    return fd


if __name__ == '__main__':
    checkTomcatStatus()
