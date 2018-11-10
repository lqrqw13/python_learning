import types

class Person(object):
    def __init__(self,new_name, new_age):
        self.name = new_name
        self.age = new_age

    def eat(self):
        print('-----{}正在吃-----'.format(self.name))
laowang = Person('老王','18')
print(laowang.name)
print(laowang.age)
laowang.addr = '北京'#给实例添加属性
Person.gender ='男'#给类添加属性
print(laowang.addr)
print(laowang.gender)

def run(self):
    print('-----{}正在跑------'.format(self.name))

laowang.run = types.MethodType(run, laowang)#给实例添加方法
laowang.run()
