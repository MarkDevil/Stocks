# coding=utf-8
import paramiko
import threading


def ssh2Server(ip, port, passwd, username, cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port, username, passwd, timeout=5)
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
            print 'exec command ....'
            #           stdin.write("Y")   #简单交互，输入 ‘Y’
            out = stdout.readlines()
            # 屏幕输出
            for o in out:
                print o,
        print '%s\tOK\n' % (ip)
        ssh.close()
    except:
        print '%s\tError\n' % (ip)


if __name__ == '__main__':
    servers = ['10.100.142.117', '10.100.142.118']
    cmd = ['cd /app/', 'pwd']
    for i in servers:
        print '%s' %(i)
        t = threading.Thread(target=ssh2Server, args=[i, 2222, 'yxgly', 'azc1rx', cmd])
        t.start()
