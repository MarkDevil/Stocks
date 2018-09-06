# coding=utf-8
__author__ = '201512010283'
import os
from flask_script import Manager
from web.stocks import stockapp

if os.path.exists('.env'):
    print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

# 通过配置创建 app
manager = Manager(app=stockapp)


@manager.command
def deploy():
    """Run deployment tasks."""
    print("deploy command")


if __name__ == '__main__':
    manager.run()
