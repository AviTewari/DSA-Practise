class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = defaultdict(int)

        for i,n in enumerate(nums):
            count[n] = i
        for i,n in enumerate(nums):
            diff = target - n
            if diff in count and count[diff]!=i:
                return [i,count[diff]]