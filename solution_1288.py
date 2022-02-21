# Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

# The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

# Return the number of remaining intervals.

# Example 1:

# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
# Example 2:

# Input: intervals = [[1,4],[2,3]]
# Output: 1
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        def removeCoveredIntervals(intervals):
            num = len(intervals)
            r = 0
            j = 0
            while(r < num):
                j = r + 1
                while(j < num):
                    if(intervals[r][0] <= intervals[j][0] and intervals[r][1] >= intervals[j][1]):
                        num-=1
                        intervals.remove(intervals[j])
                        j-=1
                    elif(intervals[r][0] >= intervals[j][0] and intervals[r][1] <= intervals[j][1]):
                        num-=1
                        intervals.remove(intervals[r])
                        r-=1
                        break
                    j+=1
                r+=1
            return num
        return removeCoveredIntervals(intervals)