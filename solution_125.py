class Solution:
    def isAlpha(self, c) -> bool:
        if (c >= 'a' and c <= 'z') or (c >= '0' and c <= '9') :
            return True
        return False
    def isPalindrome(self, s: str) -> bool:
        b = 0
        s = str.lower(s)
        f = len(s) - 1
        while True:
            
            while b < len(s)-1 and not self.isAlpha(s[b]):
                b+=1
            while f > 0 and not self.isAlpha(s[f]):
                f-=1
            if b >= f:
                return True
            if s[b] != s[f]:
                break
            
            b+=1
            f-=1
        return False
