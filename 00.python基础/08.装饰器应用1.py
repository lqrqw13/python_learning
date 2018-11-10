#对装饰器的应用，买东西讲价程序
def buy(func):
    def inner():
        print('询价')
        func()
        print('购买成功')
    return inner

def bargin(func):
    def inner():
        x = int(input('请输入你的报价: '))
        deal = x * 0.5
        print('{}:的成交价格是{}'.format(func(), deal))
    return inner

@buy
@bargin

def dog():
    return '狗'

@buy
@bargin
def pig():
    return '猪'
    

dog()
print('='*80)
pig()



