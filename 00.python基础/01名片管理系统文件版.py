cardinfo = []

def print_menu():
    print('='*50)
    print('名片管理系统v1.0')
    print('1.添加名片')
    print('2.查询名片')
    print('3.删除名片')
    print('4.查看所有名片')
    print('5.保存')
    print('6.退出')

def add_data():
    newinfo = {}
    newinfo['name'] = input('请输入姓名')
    newinfo['cell'] = input('请输入手机号码')
    cardinfo.append(newinfo)

def del_data():
    findname = input('请输入要删除的人姓名')
    check = 0
    i = 0 
    for temp in cardinfo:
        if findname == temp['name']:
            del cardinfo[i]
            check = 1
            print('删除成功')
            break
        i += 1
    if check == 0:
        print('查无此人')

def check_data():
    findname = input('请输入要查找的人姓名')
    check = 0
    for temp in cardinfo:
        if findname == temp['name']:
            print('{}的手机号码是{}'.format(temp['name'],temp['cell']))
            check = 1
            break
    if check == 0:
        print('查无此人')

def check_all_data():
    global cardinfo
    with open('database.txt') as f:
        cardinfo = eval(f.read())
    print('姓名\t\t电话')
    for temp in cardinfo:
        print('{}\t\t {}'.format(temp['name'],temp['cell']))

def save_2_file():
    with open('database.txt','w') as f:
        f.write(str(cardinfo))



def main():
    print_menu()
    while True:
        print('='*50)
        options = input('请输入要执行操作的序号')
        if options == '1':
            add_data()
            save_2_file()
        elif options == '2':
            check_data()
        elif options =='3':
            del_data()
            save_2_file()
        elif options == '4':
            check_all_data()
        elif options =='5':
            save_2_file()
        elif options =='6':
            print('程序退出')
            break
        else:
            print('输入错误')

if __name__ =='__main__':
    main()
