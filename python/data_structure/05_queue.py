class Queue(object):
    """队列"""
    def __init__(self):
        self.__queue = []

    def is_empty(self):
        return self.__queue == []

    def enqueue(self,item):
        """往队列中添加一个item元素"""
        # 1. 队列从尾巴入
        self.__queue.append(item)
        # 2. 队列从前面入
        # self.__queue.insert(0,item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        # 1. 从头出
        return self.__queue.pop(0)
        # 2. 从尾出
        # return self.__queue.pop()

    def size(self):
        """返回队列的大小"""
        return len(self.__queue)

if __name__ == "__main__":
    q = Queue()
    print(q.is_empty())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())
    print(q.is_empty())