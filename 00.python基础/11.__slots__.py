class Person(object):
    __slots__ = ('name','age')


p = Person()

p.name = 'robert'

p.age = '18'

p.addr = 'hengyang'

print(p.age)
print(p.addr)#slots元组中不包含addr，所以不能添加
