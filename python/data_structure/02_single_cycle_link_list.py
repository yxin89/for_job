#节点定义
class Node(object):
    """节点"""
    def __init__(self,item):
        self.item = item
        self.next = None


class SingleCycleLinkList(object):
    """单向循环链表"""
    def __init__(self, node=None):
        if node:
            self.__head = node
            node.next = node
        else:
            self.__head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return None
        cur = self.__head
        while cur.next != self.__head:
            print(cur.item, end=" ")
            cur = cur.next
        # 退出循环cur指向尾节点
        print(cur.item)

    def add(self,item):
        """从头部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next  != self.__head:
                cur = cur.next
            # 退出循环就是尾节点

            node.next = self.__head
            self.__head = node
            # cur.next = node
            cur.next = self.__head

    def append(self,item):
        """追加节点"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head
        
    def insert(self,pos,item):
        """插入节点"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next

            # 当循环推出后
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def search(self,item):
        """查询节点"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        if cur.item == item:
            return True
        return False

    def remove(self,item):
        """删除节点"""
        if self.is_empty():
            return None

        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.item == item:
                # 先判断此节点是否是头节点
                if cur == self.__head:
                    # 头节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                    # self.__head = cur.next
                else:
                    # 中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next

        # 退出循环，cur指向尾节点
        if cur.item == item:
            if cur == self.__head:
                # 链表只有一个节点
                self.__head = None
            else:
                pre.next = cur.next



if __name__ == "__main__":
    ll = SingleCycleLinkList()
    print(ll.is_empty())
    print(ll.length())
    
    ll.append(1)
    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.insert(3,101) # 8 1 2 101 3 4 5 6
    ll.travel()

    ll.remove(8)
    print('*'*50)
    print('length is:', ll.length())
    ll.travel()

        