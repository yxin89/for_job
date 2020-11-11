#节点定义
class Node(object):
    """节点"""
    def __init__(self,item):
        self.item = item
        self.next = None
        self.prev = None


# 单向链表
class DoubleLinkList(object):
    """单链表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

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
        node.next.prev = node

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
            node.prev = cur
        
    def insert(self,pos,item):
        """插入节点"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next

            # 当循环推出后
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

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
        while cur != None:
            if cur.item == item:
                # 先判断此节点是否是头节点
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        # 只有一个节点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next


if __name__ == "__main__":
    ll = DoubleLinkList()
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

        