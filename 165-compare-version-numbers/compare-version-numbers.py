class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = []
        v2 = []
        for i in version1.split('.'):
            v1.append(int(i))
        for i in version2.split('.'):
            v2.append(int(i))
        for i in range(max(len(v1), len(v2))):
            if i < len(v1):
                l = v1[i]
            else:
                l = 0
            if i < len(v2):
                r = v2[i]
            else:
                r = 0
            if l > r:
                return 1
            elif l<r:
                return -1
        return 0

