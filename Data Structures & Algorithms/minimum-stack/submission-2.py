class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.min = val
        else:
            self.min = min(self.min, val)
        self.stack.append((val, self.min))
        print(f"pushed: ({val}, {self.min})")

    def pop(self) -> None:
        a = self.stack.pop()
        if self.stack:
            self.min = self.stack[-1][1]
        else:
            self.min = None
        print(f"popped: {a}; new min: {self.min}")

    def top(self) -> int:
        print(f"top: {self.stack[-1][0]}")
        return self.stack[-1][0]

    def getMin(self) -> int:
        print(f"min: {self.min}")
        return self.min
