class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        outputs = [intervals[0]]
        for start, end in intervals[1:]:
            lastend = outputs[-1][1]
            if start <= lastend:
                outputs[-1][1] = max(lastend, end)
            else:
                outputs.append([start,end])

        return outputs