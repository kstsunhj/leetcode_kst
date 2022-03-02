class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        elif t == "":
            return False
        index = 0
        for r in t:
            if r == s[index]: index+=1
            if index == len(s): break
        if index == len(s):
            return True
        return False