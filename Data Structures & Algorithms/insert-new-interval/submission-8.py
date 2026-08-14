class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:       

        start = newInterval[0]
        end = newInterval[1]

        ans, check = [], False

        for i in range(0,len(intervals)):

            curr = intervals[i]

            if start < curr[0] and end < curr[0]:
                ans.append([start,end])
                print(intervals[i:])
                print(ans)
                ans += intervals[i:]
                return ans
            elif start > curr[1] and end > curr[1]:
                ans.append([curr[0],curr[1]])
            else:
                start = min(start,curr[0])
                end = max(end,curr[1])

        if not check:
            ans.append([start,end])

        return ans
        


            



            
            










