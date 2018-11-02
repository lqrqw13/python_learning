class ModelMetaclass(type):
    # attrs = {uid:('uid', "int unsigned"), 'name': ('username', "varchar(30)")....}
    def __new__(cls, name, bases, attrs):
        # 判断是否需要保存
        mappings = dict()
        for k, v in attrs.items():
            # 判断是否是指定的StringField或者IntegerField的实例对象
            if isinstance(v, tuple):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        # 删除这些已经在字典中存储的属性
        for k in mappings.keys():
            attrs.pop(k)

        # 将之前的uid/name/email/password以及对应的对象引用、类名字
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致

        return type.__new__(cls, name, bases, attrs)


class Model(metaclass = ModelMetaclass):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")
    # 当指定元类之后，以上的类属性将不在类中，而是在__mappings__属性指定的字典中存储
    # 以上User类中有 
    # __mappings__ = {
    #     "uid": ('uid', "int unsigned")
    #     "name": ('username', "varchar(30)")
    #     "email": ('email', "varchar(30)")
    #     "password": ('password', "varchar(30)")
    # }
    # __table__ = "User"

    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            # self.uid= 12345, self.name = 'Michael'...
            setattr(self, name, value)

    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v[0])
            args.append(getattr(self, k, None))


        args_temp = []
        for temp in args:
            # 判断入如果是数字类型
            if isinstance(temp, int):
                args_temp.append(str(temp))
            # ['12345',"""'Michael'""","""'test@orm.org'""","""'my-pwd'"""]
            elif isinstance(temp, str):
                args_temp.append("""'%s'""" % temp)

        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(args_temp))
        print('SQL: %s' % sql)

class User(Model):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")



u = User(uid=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
# 对应如下sql语句
# insert into User (username,email,password,uid)
# values ('Michael','test@orm.org','my-pwd',12345)