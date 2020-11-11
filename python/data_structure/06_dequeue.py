class Dequeue(object):
    """双端队列"""
    def __init__(self):
        self.__queue = []

    def is_empty(self):
        return self.__queue == []

    def add_front(self,item):
        """往队列中添加一个item元素"""
        self.__queue.insert(0,item)
    
    def add_rear(self,item):
        """往队列中添加一个item元素"""
        self.__queue.append(item)

    def pop_front(self):
        return self.__queue.pop(0)

    def pop_rear(self):
        return self.__queue.pop()

    def size(self):
        """返回队列的大小"""
        return len(self.__queue)

if __name__ == "__main__":
    dq = Dequeue()
    dq.add_front(1)
    dq.add_front(2)
    dq.add_front(3)
    dq.add_front(4)
    dq.add_rear(1)
    dq.add_rear(2)
    dq.add_rear(3)
    dq.add_rear(4)
    while dq.size():
        print(dq.pop_rear())