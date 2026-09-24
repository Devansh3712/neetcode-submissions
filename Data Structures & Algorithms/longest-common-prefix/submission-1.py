class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # strs[0] is used as a reference
        n = len(strs[0])
        for i in range(n):
            char = strs[0][i]
            # check every string at index i
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]
        return strs[0]
