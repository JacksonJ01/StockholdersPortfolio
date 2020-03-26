class Data:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedListTail:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_head(self, data):
        new = Data(data)
        if self.head is None:
            self.head = new
            if self.tail is None:
                self.tail = new
            return
        new.next = self.head
        self.head = new

    def remove_head(self):
        gone = self.head
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        return gone.data

    def add_tail(self, data):
        new = Data(data)
        if self.head is None and self.tail is None:
            self.head = new
            self.tail = new
            return
        self.tail.next = new
        self.tail = new
        return

    def return_head(self):
        if self.head is None:
            return None
        else:
            return self.head.data


class Queue:
    def __init__(self):
        self.MyQueue = LinkedListTail()

    def push(self, data):
        return self.MyQueue.add_tail(data)

    def replace_head(self, data):
        self.MyQueue.add_head(data)

    def pop(self):
        return self.MyQueue.remove_head()

    def head(self):
        return self.MyQueue.return_head()
