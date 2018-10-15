from time import sleep

def A():
    while True:
        print('===a===')
        yield
        sleep(0.5)

def B(a):
    while True:
        print('===b===')
        #'generator' object has no attribute 'next' python3中需写成__next__而不是next
        a.__next__()
        sleep(0.5)


def main():
    a = A()
    b = B(a)

if __name__ == '__main__':
    main()
