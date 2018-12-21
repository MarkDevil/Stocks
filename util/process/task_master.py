# coding=utf-8
import Queue
import random
from multiprocessing.managers import BaseManager

task_queue = Queue.Queue()
result_queue = Queue.Queue()


# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass


# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('10.29.128.145', 5000), authkey=b'abc')
# 启动Queue
manager.start()

# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去:
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# 从result队列读取结果:
print('Try get results...')
while True:
    for i in range(10):
        try:
            r = result.get(timeout=3)
            print('Result: %s' % r)
        except Exception:
            print("Get result data failied, results queue is empty!")
# 关闭:
manager.shutdown()
print('master exit.')
