from multiprocessing import Pool
import time
import os

def test():
    print('进程池中的进程---pid={}, ppid={}'.format(os.getpid, os.getppid()))
    for i in range(3):
        print('==={}==='.format(i))
        time.sleep(1)
    return 'haha'

def test2(args):
    print('===callback func--pid = {}, ppid = {}'.format(os.getpid(), os.getppid()))
    print('===call back func--args= {}'.format(args))

def main():

    pool = Pool(3)
    pool.apply_async(func = test, callback = test2)
    

    while True:
        time.sleep(1)
        print('====主进程-pid = {}'.format(os.getppid()))

if __name__ == '__main__':
    main()