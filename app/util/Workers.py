#coding = utf-8
__author__ = 'mingfengma'

import Queue
import sys
import threading
import time
import requests


class Worker(threading.Thread):
    def __init__(self, workQueue, resultQueue, **kwds):
        threading.Thread.__init__(self, **kwds)
        self.setDaemon(True)
        self.workQueue = workQueue
        self.resultQueue = resultQueue

    def run(self):
        while 1:
            try:
                callable, args, kwds = self.workQueue.get(False)
                res = callable(*args, **kwds)
                self.resultQueue.put(res)
            except Queue.Empty:
                break

class WorkManager:
    def __init__(self, num_of_workers = 10):
        self.workQueue = Queue.Queue()
        self.resultQueue = Queue.Queue()
        self.workers = []
        self._recruitThreads(num_of_workers)

    def _recruitThreads(self, num_of_workers):
        for i in range(num_of_workers):
            worker = Worker(self.workQueue, self.resultQueue)
            self.workers.append(worker)

    def start(self):
        for w in self.workers:
            w.start()

    def waitforfinish(self):
        while len(self.workers):
            worker = self.workers.pop()
            worker.join()
            if worker.isAlive() and not self.workQueue.empty():
                self.workers.append(worker)

        print 'all jobs finished '

    def add_job(self, callable, *args, **kwds):
        self.workQueue.put((callable, args, kwds))

    def get_result(self, *args, **kwargs):
        return self.resultQueue.get(args, kwargs)

def download_file(url):
    print requests.get(url).text

def main():
    try:
        num_of_threads = int(sys.argv[1])
    except:
        num_of_threads = 10
    _start_time = time.time()
    wm = WorkManager(num_of_threads)
    urls = ['https://www.hao123.com/?tn=95399240_s_hao_pg'] * 100
    for i in urls:
        wm.add_job(download_file, i)
    wm.start()
    wm.waitforfinish()
    print time.time() - _start_time

def runlianjia():
    wm = WorkManager(10)


if __name__ == '__main__':
    main()



