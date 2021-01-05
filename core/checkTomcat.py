# coding = utf-8
__author__ = 'mingfengma'

import paramiko
import util.logutil

HOSTS = ['192.168.18.45']
PORT = 22
USER = 'root'
PASSWD = 'qwe123ASD()'
PROJECTPATH = '/houbank/server'
PROJECTNAMES = ['hbadmin', 'tomcat-hbadmin-api',
                'tomcat-aloan-las', 'tomcat-aloan-oms',
                'tomcat-aloan-plas-api', 'tomcat-aloan-plas-task']
logger = util.logutil.Log("info").initlogger()
global ssh


def sshInit():
    global ssh
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


def sshToServer():
    pass


def checkTomcatStatus():
    fd = {}
    sshInit()
    for host in HOSTS:
        ssh.connect(host, PORT, USER, PASSWD)
        for pname in PROJECTNAMES:

            stdin, stdout, stderr = \
                ssh.exec_command('ps -ef | grep ' + PROJECTPATH + '/' + pname + '| grep -v grep | '
                                                                                'awk \'{print $2}\'')
            data = stdout.read()
            pids = str(data).split('\n')
            for pid in pids:
                if pid is None or pid is '':
                    pids.remove(pid)
                else:
                    continue
            logger.info("PID number is " + str(pids))
            if data is not None:
                fd[host + pname] = 'ok'
            else:
                fd[host + pname] = 'bad'

        stdin, stdout, stderr = \
            ssh.exec_command('docker ps | grep mls')
        data1 = stdout.read()
        # logger.info("ret msg '%s'", str(data1).split(" "))

    ssh.close()
    logger.info("Check status is '%s'", fd)
    return fd


def checkdockerStatus():
    pass


if __name__ == '__main__':
    checkTomcatStatus()
