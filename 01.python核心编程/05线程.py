import time
from threading import Thread #多线程
import os
from multiprocessing import Process #多进程


def test():
    print('I am tough guy! {}'.format(os.getpid()))
    time.sleep(1)

# if __name__ == '__main__':
#     for i in range(5):
#         process = Process(target = test)
#         process.start()


for i in range(5):
    thread = Thread(target= test)
    thread.start()
