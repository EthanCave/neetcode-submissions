class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack and val < self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.insert(len(self.min_stack) - 1, val)

    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            self.stack.pop()
            self.min_stack.pop()
        else:
            self.stack.pop()
            self.min_stack.pop(len(self.min_stack) - 2)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1] #note now O(1)
