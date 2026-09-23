class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = [0] * 26
        for char in s:
            # ascii value of 'a' is 97
            chars[ord(char) - 97] += 1
        for char in t:
            chars[ord(char) - 97] -= 1
        for count in chars:
            if count != 0:
                return False
        return True