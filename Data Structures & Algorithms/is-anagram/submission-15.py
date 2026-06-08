class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = defaultdict(int)

        for idx in range(len(s)):
            count[s[idx]] += 1
            count[t[idx]] -= 1

        return all(v == 0 for v in count.values())