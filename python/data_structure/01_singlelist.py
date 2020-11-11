#节点定义
class Node(object):
    """节点"""
    def __init__(self,item):
        self.item = item
        self.next = None


# 单向链表
class SingleLinkList(object):
    """单链表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur != None:
            print(cur.item, end=" ")
            cur = cur.next
        print()

    def add(self,item):
        """从头部添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self,item):
        """追加节点"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
        
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
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False

    def remove(self,item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur != None:
            if cur.item == item:
                # 先判断此节点是否是头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next


if __name__ == "__main__":
    ll = SingleLinkList()
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
    ll.remove(8)

    print('*'*50)
    print('length is:', ll.length())
    ll.travel()

        