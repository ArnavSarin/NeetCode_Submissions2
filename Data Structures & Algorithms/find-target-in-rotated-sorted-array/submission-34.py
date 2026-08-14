class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_rotations, max_rotations = 0, len(nums)-1

        if len(nums) == 1 and nums[0] == target:
            return 0
            
        while min_rotations < max_rotations:
            mid = (min_rotations + max_rotations)//2 

            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[max_rotations]:
                min_rotations = mid + 1  
            else:
                max_rotations = mid 


        if nums[-1] >= target >= nums[min_rotations]: 
            max_rotations = len(nums) - 1
        else:
            min_rotations, max_rotations = 0, min_rotations - 1
        
        while min_rotations <= max_rotations:
            mid = (min_rotations + max_rotations)//2

            if target == nums[mid]:
                return mid
            elif nums[mid] > target:
                max_rotations = mid - 1
            else:
                min_rotations = mid + 1
        
        return -1

            




        



        
        


