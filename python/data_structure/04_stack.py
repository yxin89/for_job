class Stack(object):
    """栈"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        """添加一个新的元素item到栈顶"""
        self.items.append(item)

    def pop(self):
        """弹出栈顶元素"""
        return self.items.pop()

    def peek(self):
        """返回栈顶元素"""
        length = self.size()
        if length:
            return self.items[length - 1]
        else:
            return None

    def size(self):
        """返回栈的元素个数"""
        return len(self.items)

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.size())
    print(s.pop())
    print(s.pop())
    print(s.peek())
    print(s.pop())
    print(s.is_empty())