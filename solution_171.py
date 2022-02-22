# Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 

# Example 1:

# Input: columnTitle = "A"
# Output: 1
# Example 2:

# Input: columnTitle = "AB"
# Output: 28
# Example 3:

# Input: columnTitle = "ZY"
# Output: 701

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        def ESCN(columnTitle):
            res = 0
            index = len(columnTitle)
            for r in columnTitle:
                index-=1
                res += (ord(r) - 65 + 1) * pow(26,index)

            return res
        return(ESCN(columnTitle))
        