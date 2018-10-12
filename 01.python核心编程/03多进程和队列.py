from multiprocessing import Manager, Pool
import os,time,random

def write(q):
    print("writer启动(%s),父进程为(%s)"%(os.getpid(),os.getppid()))
    for i in "dongGe":
        q.put(i)

def read(q):
    print("reader启动(%s),父进程为(%s)"%(os.getpid(),os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到消息：%s"%q.get(True))

def main():
    q = Manager().Queue()
    pool = Pool()
    #使用阻塞模式创建进程，这样就不需要在reader中使用死循环了，可以让writer完全执行完成后，再用reader去读取
    pool.apply(write, (q,))
    pool.apply(read, (q,))
    pool.close()
    pool.join()
    print("(%s) End"%os.getpid())

if __name__ == '__main__':
    main()