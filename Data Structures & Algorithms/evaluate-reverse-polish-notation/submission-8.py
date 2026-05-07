class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {'+': lambda a, b: a + b,
                      '-': lambda a, b: a - b,
                      '/': lambda a, b: int(a / b),
                      '*': lambda a, b: a * b,}
        stack = []

        for token in tokens:  
            if token in operations:
                a, b = stack.pop(), stack.pop()
                stack.append(operations[token](b, a))
                continue
            stack.append(int(token)) 

        return stack[-1] if stack else None