# coding=utf-8
import psutil


def cpu_times():
    ret = psutil.cpu_percent(2, True)
    print(ret)


def net_connections():
    ret = psutil.net_connections()
    print(ret)


if __name__ == '__main__':
    while True:
        cpu_times()
        net_connections()
