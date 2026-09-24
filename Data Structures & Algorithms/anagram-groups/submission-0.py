from collections import defaultdict

class Solution:
    def char_count(self, s: str) -> List[int]:
        chars = [0] * 26
        for char in s:
            chars[ord(char) - 97] += 1
        return chars

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = tuple(self.char_count(s))
            groups[key].append(s)
        return list(groups.values())