from collections import deque

class MyQueue:
    def __init__(self):
        self.stack = deque()
        self.temp = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        while len(self.stack) > 1:
            self.temp.append(self.stack.pop())
        result = self.stack.pop()
        while self.temp:
            self.stack.append(self.temp.pop())
        return result

    def peek(self) -> int:
        while self.stack:
            self.temp.append(self.stack.pop())
        result = self.temp[-1]
        while self.temp:
            self.stack.append(self.temp.pop())
        return result
        

    def empty(self) -> bool:
        return not self.stack
