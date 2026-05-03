class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for st in strs:
            char = [0] * 26
            for s in st:
                char[ord(s) - ord('a')] += 1
            output[tuple(char)].append(st)

        return list(output.values())
