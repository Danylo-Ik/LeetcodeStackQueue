class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x: int) -> None:
        if not self.head:
            self.head = Node(x)
            self.tail = self.head
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next

    def pop(self) -> int:
        if self.head:
            value = self.head.value
            self.head = self.head.next
            return value
        return None

    def peek(self) -> int:
        if self.head:
            return self.head.value
        return None

    def empty(self) -> bool:
        return not self.head
