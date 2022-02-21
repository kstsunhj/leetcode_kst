# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

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