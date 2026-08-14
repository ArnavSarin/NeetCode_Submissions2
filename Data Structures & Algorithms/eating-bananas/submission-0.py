import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_hours, max_hours = 1, max(piles)

        ans = float('inf')
        while min_hours <= max_hours:
            mid = (min_hours+max_hours)//2

            hours = 0
            for i in piles:
                hours += math.ceil(i/mid)
            
            if hours <= h:
                ans = min(mid, ans)
                max_hours = mid - 1
            else:
                min_hours = mid + 1

        return ans


