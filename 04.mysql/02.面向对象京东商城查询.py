from pymysql import *

class JD(object):
    def __init__(self):
        self.conn = connect(port=3306, host='localhost', user='root', password='lx131313', database='JD', charset='utf8')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()
        
    def get_info(self,sql):
        self.cursor.execute(sql)
        lines = self.cursor.fetchall()
        for temp in lines:
            print(temp)     
    # get all info        
    def a(self):
        sql = 'select * from goods;'
        self.get_info(sql)
    # get cates info
    def b(self):
        sql='select name from goods_cates;'
        self.get_info(sql)
    # get brand info
    def c(self):
        sql='select name from goods_brands;'
        self.get_info(sql)
    # print menu
    @staticmethod
    def menu():
        print('====mysql inquiry system====')
        print('1. get all info')
        print('2. get all cate_info')
        print('3. get all brand_info')
        print('4. exit')

    def run(self):
        while True:
            self.menu()
            command = input('please input your comannd with index number:')
            if command == '1':
                self.a()
            elif command =='2':
                self.b()
            elif command =='3':
                self.c()
            elif command =='4':
                break
            else:
                print('input error')
        
    

def main():
    # create an object jd
    jd = JD()
    # use method run
    jd.run()

if __name__=='__main__':
    main()
