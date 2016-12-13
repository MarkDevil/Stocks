__author__ = 'mingfengma'

import paramiko
import time
import schedule

HOSTS = ['10.100.142.117']
PORT = 2222
USER = 'yxgly'
PASSWD = 'azc1rx'


def checkTomcatStatus():
    fd = {}
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for host in HOSTS:
        ssh.connect(host, PORT, USER, PASSWD)
        stdin, stdout, stderr = ssh.exec_command('ps -ef | grep tomcat-financial | grep -v grep | awk \'{print $2}\'')
        data = stdout.read()
        print data
        if data is not None:
            fd[host] = 'ok'
        else:
            fd[host] = 'bad'
    ssh.close()
    return fd

schedule.every(10).seconds.do(checkTomcatStatus)

if __name__ == '__main__':
    while 1:
        schedule.run_pending()
        time.sleep(10)