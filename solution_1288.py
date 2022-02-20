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