from collections import deque

class FreqStack:
    def __init__(self):
        self.stack = deque()
        self.freq_dict = {}

    def push(self, val: int) -> None:
        if val in self.freq_dict:
            self.freq_dict[val] += 1
        else:
            self.freq_dict[val] = 1

        self.stack.append(val)

    def pop(self) -> int:
        max_freq_val = None
        max_freq = 0
        for key, value in self.freq_dict.items():
            if value >= max_freq:
                max_freq = value
                max_freq_val = key

        popped = False
        temp = deque()
        for i in reversed(self.stack):
            if self.freq_dict[i] == max_freq:
                max_freq_val = i
                break
        while self.stack:
            if self.stack[-1] == max_freq_val and not popped:
                self.stack.pop()
                popped = True
            else:
                temp.append(self.stack.pop())

        while temp:
            self.stack.append(temp.pop())

        self.freq_dict[max_freq_val] -= 1
        if self.freq_dict[max_freq_val] == 0:
            del self.freq_dict[max_freq_val]

        return max_freq_val
