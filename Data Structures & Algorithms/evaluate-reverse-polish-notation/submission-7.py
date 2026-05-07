class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {'+': lambda a, b: a + b,
                      '-': lambda a, b: a - b,
                      '/': lambda a, b: int(a / b),
                      '*': lambda a, b: a * b,}
        stack = [0]

        # tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        for token in tokens:  
            if token in operations:
                a = stack.pop()
                b = stack.pop()
                stack.append(operations[token](b, a))
                continue
            stack.append(int(token)) # [22]

        return stack[-1] if stack else None