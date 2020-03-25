class Data:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_head(self, data):
        new = Data(data)
        new.next = self.head
        self.head = new
        return

    def remove_head(self):
        gone = self.head
        self.head = self.head.next
        return gone.data

    def return_head(self):
        if self.head is None:
            return None
        else:
            return self.head.data


class Stack:
    def __init__(self):
        self.MyStack = LinkedList()

    def push(self, data):
        return self.MyStack.add_head(data)

    def pop(self):
        return self.MyStack.remove_head()

    def head(self):
        return self.MyStack.return_head()
