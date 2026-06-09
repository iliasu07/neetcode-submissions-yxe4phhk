class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        length = 26
        for st in strs:
            char = [0] * length
            for s in st:
                char[ord(s)- ord('a')] += 1
            anagrams[tuple(char)].append(st)
        return list(anagrams.values())