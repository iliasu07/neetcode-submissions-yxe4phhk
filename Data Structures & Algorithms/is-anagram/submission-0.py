from collections import defaultdict, Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #s_dict = defauldtict(int)
#
        #for n in s:
        #    s_dict[c] += 1

        return Counter(s) == Counter(t)