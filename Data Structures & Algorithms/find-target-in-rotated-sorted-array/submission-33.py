class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_rotations, max_rotations = 0, len(nums)-1

        if len(nums) == 1 and nums[0] == target:
            return 0
            
        while min_rotations < max_rotations:
            mid = (min_rotations + max_rotations)//2 
            print(mid)

            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[max_rotations]:
                min_rotations = mid + 1  
            else:
                max_rotations = mid 

        print(min_rotations)

        if nums[-1] >= target >= nums[min_rotations]: 
            max_rotations = len(nums) - 1
        else:
            min_rotations, max_rotations = 0, min_rotations - 1
            #MAYBE NEGATIVE ONE

        print("GOT HERE 0")
        print(min_rotations)
        print(max_rotations)
        
        while min_rotations <= max_rotations:
            mid = (min_rotations + max_rotations)//2

            if target == nums[mid]:
                print("GOT HERE 0")
                return mid
            elif nums[mid] > target:
                print("GOT HERE 1")
                max_rotations = mid - 1
            else:
                print("GOT HERE 2")
                min_rotations = mid + 1
        
        return -1

            




        



        
        


