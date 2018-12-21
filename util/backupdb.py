# coding=utf-8
import os
import sys
import time

host = '127.0.0.1'
port = '3306'
user = 'root'
passwd = 'root'
dbname = 'automation'
backup_path = '/Users/mark/backup/mysql'
filename = time.strftime('%Y%m%d_%H%M%S')

backup_file = backup_path + filename


class BackUpDb:

    def __init__(self):
        if not os.path.exists(backup_file):
            os.makedirs(backup_file)
            print("备份目录创建成功")
        else:
            print("备份目录已经存在")

    def backup_db(self, dbname):
        dump = "mysqldump {dbname} -h{host} -u{user} -p{passwd} > {backup_file}/{dbname}.sql".format(
            dbname=dbname, host=host, user=user, passwd=passwd, backup_file=backup_file)
        print("执行备份语句为:" + dump)
        exit_stats = os.system(dump)
        print("执行返回状态:" + str(exit_stats))

    '''
        返回退出状态
    '''

    def backup_table(self, dbname, tablename):
        # type: (object, object) -> int
        dump = "mysqldump {dbname} -h{host} -u{user} -p{passwd} -t {tablename} > {backup_file}/{tablename}.sql".format(
            dbname=dbname, host=host, user=user, passwd=passwd, tablename=tablename, backup_file=backup_file)

        print("执行备份语句为:" + dump)
        exit_stats = os.system(dump)
        print("执行返回状态:" + str(exit_stats))
        if exit_stats == 0:
            print("执行成功")
        else:
            print("执行失败,返回状态为:{}".format(exit_stats))
        return exit_stats

    def tar_file(self):
        pass

    @staticmethod
    def run(argv):
        backup = BackUpDb()
        if argv.__len__() >= 3 and argv[2] is not None:
            print(str(argv))
            print("开始备份数据库表")
            backup.backup_table(argv[1], argv[2])
        else:
            print("开始备份整个数据库")
            backup.backup_db(argv[1])


'''
    :arg[1] 数据库名
    :arg[2] 数据库表名
    
'''
if __name__ == '__main__':
    BackUpDb.run(sys.argv)
