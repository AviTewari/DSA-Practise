class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = defaultdict(int)
        for i,n in enumerate(nums):
            c[n] += 1
        res =[k for k,v in sorted(c.items(), key = lambda x: x[1], reverse = True)]
        return res[:k]