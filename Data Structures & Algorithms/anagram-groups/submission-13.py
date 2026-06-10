class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        length = 26
        for st in strs:
            char = [0] * length
            for s in st:
                char[ord(s) - ord('a')] += 1
            anagram[tuple(char)].append(st)
        return list(anagram.values())