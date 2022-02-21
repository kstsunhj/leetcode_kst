# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def MoTSA(nums1, nums2):
            m = len(nums1)
            n = len(nums2)
            tr = int((m + n)/2)
            templ = 0
            tempr = 0
            tl = (tr - 1) if tr == (m + n)/2 else -1
            i = 0
            j = 0
            index = 0
            while((i < m) and (j < n)):
                templ = tempr
                if(nums1[i] >= nums2[j]):

                    tempr = nums2[j]
                    j+=1
                else:

                    tempr = nums1[i]
                    i+=1
                if(index == tr):
                    if(tl != -1):
                        return (templ + tempr)/2
                    elif(tl == -1):
                        return tempr
                index+=1
            if(tl == -1):
                if(m == i):
                    return nums2[(tr - index) + j]
                elif(n == j):
                    return nums1[(tr - index) + i]
            else:
                if(tl == index - 1):
                    if(m == i):
                        return (nums2[j] + tempr)/2
                    elif(n == j):
                        return (nums1[i] + tempr)/2
                else:
                    if(m == i):
                        return (nums2[(tr - index) + j] + nums2[(tr - index) + j - 1])/2
                    elif(n == j):
                        return (nums1[(tr - index) + i] + nums1[(tr - index) + i - 1])/2
        return MoTSA(nums1,nums2)