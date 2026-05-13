class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(c for c in s if c.isalnum())
        left, right = 0, len(string) - 1

        while left <= right:
            if string[left].lower() != string[right].lower():
                return False
            left += 1
            right -= 1
        return True
            
