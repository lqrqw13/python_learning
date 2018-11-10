class Test(object):
    def __init__(self):
        self.__num = 100

#    def set_num(self,newnum):
    @property
    def num(self):
        return self.__num

#    def get_num(self):
    @num.setter
    def num(self,newnum):
        self.__num = newnum

#    num = property(get_num, set_num)

t = Test()
'''
print(t.get_num())
t.set_num(50)
print(t.get_num())
'''
t.num = 200
print(t.num)
