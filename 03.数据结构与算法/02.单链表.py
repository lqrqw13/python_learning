class Node(object):
    def __init__(self,elem):
        self.elem = elem
        self.next = None

        
class SingleList(object):
    '''单链表'''
    def __init__(self, node = None):
        self.head = node

    def is_empty(self):
        '''判断是否为空'''
        return self.head == None
    
    def length(self):
        '''计算长度'''
        count = 0
        cur = self.head
        while cur != None:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        '''遍历链表'''
        cur = self.head
        while cur != None:
            print(cur.elem, end = " ")
            cur = cur.next

    def append(self, item):
        '''末尾添加节点'''
        node = Node(item)
        cur = self.head
        if self.is_empty():
            self.head = node
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = node 
        
    def add(self, item):
        '''链表表头r添加节点'''
        node = Node(item)
        node.next = self.head
        self.head = node

    def insert(self, pos, item):
        '''指定位置插入元素'''
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(item)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length()-1):
            self.append(item)
        # 找到指定位置
        else:
            node = Node(item)
            count = 0
            cur = self.head
            while count < (pos - 1):
                count += 1
                cur = cur.next
            # 先将新节点node的next指向插入位置的节点
            node.next = cur.next
             # 将插入位置的前一个节点的next指向新节点
            cur.next = node

    def search(self, item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self.head
        while cur != None:
            if cur.elem == item:
                return True
            cur = cur.next
        return False
    
    def remove(self,item):
        cur = self.head
        pre = None
        while cur != None:
            # 找到了指定元素
            if cur.elem == item:
                #如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self.head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next     
def main():
    ll = SingleList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2,4)
    print ("length:", ll.length())
    ll.travel()
    print(ll.search(3))
    print(ll.search(5)) 
    ll.remove(1)
    print("length:", ll.length())
    ll.travel()
if __name__ == "__main__":
    main()
