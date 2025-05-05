class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        sum = 0
        p_sum = {0:1}
        for i in nums:
            sum+=i
            diff = sum - k
            res+= p_sum.get(diff,0)
            p_sum[sum] = 1 + p_sum.get(sum,0)
        return res

