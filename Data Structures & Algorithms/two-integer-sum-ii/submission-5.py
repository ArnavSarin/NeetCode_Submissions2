class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm = defaultdict()

        for i in range(0,len(numbers)):
            hm[target-numbers[i]] = i

        for i in range(0,len(numbers)):
            if  numbers[i] in hm:
                return [i+1,hm[numbers[i]]+1]
        
        return []