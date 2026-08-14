class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        if(len(nums)==0):
            return 0

        max_sum = 1
        for i in seen:
            if (i-1) not in seen:
                counter = 1
                while i + counter in seen:
                    counter += 1
                    max_sum = max(max_sum, counter)
        return max_sum


                