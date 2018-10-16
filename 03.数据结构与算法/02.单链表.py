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

def main():
    ll = SingleList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    ll.append(2)
    ll.add(3)
    ll.travel()
    
    
if __name__ == "__main__":
    main()
