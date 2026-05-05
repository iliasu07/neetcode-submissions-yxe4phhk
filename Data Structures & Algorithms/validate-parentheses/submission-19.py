class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        brackets = { "}" : "{", ")" : "(", "]" : "["}
        stack = []

        # s = "([])"   "]()"  stack = [ ([ ]
        for b in s:  
            if b in brackets:
                if stack and stack[-1] == brackets[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)

        return len(stack) == 0
                