from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = []
        for r in nums:
            if not s or (r not in s):
                s.append(r)
            elif r in s:
                s.pop(s.index(r))
        return s[0]
ans = Solution()
print(ans.singleNumber([1]))
