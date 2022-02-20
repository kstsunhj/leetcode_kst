class Solution:#do it myself
    def lengthOfLongestSubstring(self, s: str) -> int:
        def LSWRC(s):
            r = 0
            max = 0
            while(r < len(s)):
                j = r
                res = []
                max_temp = 0
                while(j < len(s)):
                    if(s[j] not in res):
                        res.append(s[j])
                        max_temp+=1
                    else:
                        break
                    j+=1
                max = max if max > max_temp else max_temp
                r += 1
                if((len(s) - r) <= max):
                    break
            return max
        return LSWRC(s)
            
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        sub_str = ''
        max_len = 0
        
        for w in s:
            while w in sub_str:
                sub_str = sub_str[1:]
            else:
                sub_str += w
                max_len = max(len(sub_str), max_len)
        
        return max_len