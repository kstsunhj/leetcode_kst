res = []
class Solution:
    def isPalindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start+=1
            end-=1
        return True
    def helper(self, s,start,out,res):
        if start == len(s):
            res.append(out.copy())
            return 
        for i in range(start, len(s)):
            if not self.isPalindrome(s,start,i):
                continue
            out.append(s[start:i + 1])
            self.helper(s,i+1,out,res)
            out.pop()
    def partition(self, s):
        res = []
        out = []
        self.helper(s, 0, out, res)
        return res
