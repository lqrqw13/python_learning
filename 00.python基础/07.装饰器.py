'''
一个装饰器
def outer(func):
    def inner():
        print('正在验证')
        func()
    return inner

@outer
def f1():
    print('-----F1----')

@outer
def f2():
    print('-----F2----')

#f1 = outer(f1)
f1()
f2()
'''

#两个装饿器

def make_bold(fn):
    def wrapped():
        print('----1----')
        return '</b>' + fn() + '</b>'
    return wrapped

def make_italic(fn):
    def wrapped():
        print('----2----')
        return '<i>' + fn() + '<i>'
    return wrapped

@make_bold
@make_italic
def test3():
    print('----3----')
    return 'hello wold'

test3()
#print(ret)
