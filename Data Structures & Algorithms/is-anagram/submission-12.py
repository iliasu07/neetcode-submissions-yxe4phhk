class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = defaultdict(int)
        countT = defaultdict(int)

        for idx in range(len(s)):
            countS[s[idx]] += 1
            countT[t[idx]] += 1

        return countS == countT