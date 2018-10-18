class Stack(object):
    def __init__(self):
        self.__list = []

    def push(self, item):
        '''添加一一个新的元素item到s栈顶'''
        self.__list.append(item)
        
         
    def pop(self):
        '''弹出栈顶元素'''
        return self.__list.pop()

    def peek(self):
        '''返回栈顶元素'''
        if self.__list:
            return self.__list[-1] 
        else:
            return None

    def is_empty(self):
        '''判断栈是否为空'''
        return not self__list

    def size(self):
        '''返回栈的元素个数'''
        return len(self.__list)

def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    
    
    
if __name__ == '__main__':
    main()
