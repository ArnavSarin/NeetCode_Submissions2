class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for i in strs:
            j = ''.join(sorted(i))
            hm[j].append(i)

        return [i for i in hm.values()]