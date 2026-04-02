class Solution:
    def isValid(self, s: str) -> bool:
        # while "()" in s or "[]" in s or "{}" in s:
        #     s = s.replace("()", "")
        #     s = s.replace("[]", "")
        #     s = s.replace("{}", "")
        # 
        # return (s == "")

        #([{}]) stack= ([{

        brackets = { "}" : "{", "]" : "[", ")" : "("}
        stack = []
        n = len(s)
        if n % 2 != 0:
            return False

        for b in s:
            if b in brackets:
                if stack and stack[-1] == brackets[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b) 

        return len(stack) == 0

        
        
            

        