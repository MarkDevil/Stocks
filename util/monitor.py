# coding=utf-8
import time

import psutil
import requests
from requests import Response


def cpu_times():
    ret = psutil.cpu_percent(2, True)
    print(ret)


def net_connections():
    ret = psutil.net_connections()
    print(ret)


def check_tomcat_stats():
    resp = requests.get("http://localhost:8080")  # type: Response
    print(resp.status_code)


if __name__ == '__main__':

    while True:
        # cpu_times()
        # net_connections()
        check_tomcat_stats()
        time.sleep(2)
