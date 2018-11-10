class Test(object):
    def __init__(self,name):
        self.name = name

    def __getattribute__(self, item):
        print('====打印日志====')
        return object.__getattribute__(self, item)

t = Test('robert')
print(t.name)
