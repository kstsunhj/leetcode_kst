from typing import List
#寫一個function，把list裡的str放進來能完成的返回True
#先一個一個進，再兩個兩個可以用dp來做

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for r in wordDict:
            Counter = 0
            while s.find(r)!=-1:
                Counter += 1
                s = s[:s.find(r)] + s[s.find(r) + len(r):]
            if Counter == 0:
                return False
        return True
ans = Solution()
print(ans.wordBreak(s = "leetcode", wordDict = ["leet","code"]))