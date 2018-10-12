#在windows环境下测试分布式代码过程中，利用fork()生成的child processes的代码须放在main模块中，否则将会报错

from multiprocessing import Process
import time

def test():
    while True:
        print('===test===')
        time.sleep(1)

def main():
    p = Process(target = test)
    p.start()
    while True:
        print('===main===')
        time.sleep(1)

if __name__ == '__main__':
    main()
