# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         count = defaultdict(list)
#         for s in strs:
#             res = [0]*26
#             for c in s:
#                 res[ord(c) - ord("a")] +=1
#             count[tuple(res)].append(s)
#         return count.values()

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for i in strs:
            res = [0]*26
            for c in i:
                res[ord(c) - ord("a")] += 1
            count[tuple(res)].append(i)
        return list(count.values())