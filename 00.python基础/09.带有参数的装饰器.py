def func_outter(args):
    def test(func):
        def inner():
            print('----日志记录----')
            print(args)
            func()
        return inner
    return test

@func_outter('abc')
def func():
    print('----func----')

func()
