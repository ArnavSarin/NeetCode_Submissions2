class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_rotations, max_rotations = 0, len(nums)-1

        while min_rotations < max_rotations:
            mid = (min_rotations + max_rotations)//2

            if nums[mid] >= nums[max_rotations]:
                min_rotations = mid + 1
            else:
                max_rotations = mid

        return nums[min_rotations]
