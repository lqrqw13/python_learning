from pymysql import *

conn = connect(port=3306, host='localhost', user='root', password='lx131313', database='JD', charset='utf8')
cursor = conn.cursor()


print('====mysql inquiry system====')
print('1. get all info')
print('2. get all cate_info')
print('3. get all brand_info')
print('4. exit')


def a():
    cursor.execute('select * from goods;')
    lines = cursor.fetchall()
    for temps in lines:
        print(temps)     
def b():
    cursor.execute('select name from goods_cates;')
    lines = cursor.fetchall()
    for temps in lines:
        print(temps)

def c():
    cursor.execute('select name from goods_brands;')
    lines = cursor.fetchall()
    for temps in lines:
        print(temps)
    
while True:
    command = int(input('please input your comannd with index number:'))
    if command == 1:
        a()
    elif command ==2:
        b()
    elif command ==3:
        c()
    elif command ==4:
        break
    else:
        print('the command you given is wrong')

cursor.close()
conn.close()
