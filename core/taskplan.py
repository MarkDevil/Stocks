# coding=utf-8

import schedule
import time


def job():
    print("I'm working...")


schedule.every(5).seconds.do(job)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
