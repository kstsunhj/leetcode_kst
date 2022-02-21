class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def majority(nums):
            nums.sort()
            n = len(nums)
            return nums[int(n/2)]
        return majority(nums)