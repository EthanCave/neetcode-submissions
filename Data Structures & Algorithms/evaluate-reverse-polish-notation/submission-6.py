class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+', '-', '/', '*']:
                if token == '+':
                    result = stack.pop() + stack.pop()
                if token == '-':
                    result = stack.pop(len(stack) - 2) - stack.pop()
                if token == '/':
                    result = int(stack.pop(len(stack) - 2) / stack.pop())
                if token == '*':
                    result = stack.pop() * stack.pop()
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[0]

