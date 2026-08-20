class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        sortedIntervals = sorted(intervals, key=lambda x:x[1], reverse=False)
        temp, ans = sortedIntervals[0], 0

        for i in range(1,len(sortedIntervals)):
            start, end = sortedIntervals[i]

            if start < temp[1] :
                ans += 1
            else:
                temp = [start,end]

        return ans

