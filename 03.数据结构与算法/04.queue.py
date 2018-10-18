class Queue(object):
    '''队列的实现'''
    # Queue() 创建一个空的队列
    def __init__(self):
        self.__list = []
    # enqueue(item) 往队列中添加一个item元素

    def enqueue(self,item):
        self.__list.append(item)


    # dequeue() 从队列头部删除一个元素
    def dequeue(self):
        if not self.__list:
            return None 
        return self.__list.pop(0) 


    # is_empty() 判断一个队列是否为空
    def is_empty(self):
        return not self.__list


    # size() 返回队列的大小
    def size(self):
        return len(self.__list)

def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue()) 

if __name__ == "__main__":
    main()
