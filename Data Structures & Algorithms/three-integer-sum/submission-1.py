class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hm = defaultdict()

        for i in range(0,len(nums)):
            hm[0-nums[i]] = i

        print(hm)

        ans = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                total = nums[i]+nums[j]
                if total in hm:
                    idx = hm[total]
                    if i != idx and j!= idx and idx > i and idx > j:
                        print("GOT HERE 0")
                        print(i)
                        print(j)
                        print(idx)
                        temp = sorted([nums[i],nums[j],nums[idx]])
                        ans.append(temp)

        ans = set([(i[0],i[1],i[2]) for i in ans])

        return [[i[0],i[1],i[2]] for i in ans]
        
