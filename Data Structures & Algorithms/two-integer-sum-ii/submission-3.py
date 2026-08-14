class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm = defaultdict()

        for i in range(0,len(numbers)):
            other_number = target-numbers[i]
            hm[other_number] = i

        for i in range(0,len(numbers)):
            current_number = numbers[i]
            if  current_number in hm:
                return [i+1,hm[current_number]+1]
        
        return []