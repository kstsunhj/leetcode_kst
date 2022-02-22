# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
          if len(s) <= 1 or s == s[::-1]:
            return s
          else:
            maxlen = 1
            start = 0
            for i in range(1, len(s)):
                odd = s[i-maxlen-1 : i+1]
                even = s[i-maxlen : i+1]
                if i-maxlen-1 >= 0 and odd == odd[::-1]:
                    start = i-maxlen-1
                    maxlen = maxlen + 2
                    continue
                if even == even[::-1]:
                    start = i-maxlen
                    maxlen = maxlen + 1
            return s[start: start+maxlen]
    
                