class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = Counter(nums)

        print(hm)
        ans = sorted(hm.items(), key=lambda x:x[1], reverse=True)
        print(ans)
        return [i[0] for i in ans][:k]

        