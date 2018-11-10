#利用yield，创建多任务——协程
import time

def test1():
    while True:
        print('1')
        yield None

def test2():
    while True:
        print('2')
        yield None

t1 = test1()#创建一个生成器对象
t2 = test2()
while True:
    next(t1)
    time.sleep(1)
    next(t2)
    time.sleep(1)
    
