class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(int, version1.split('.')))
        version2 = list(map(int, version2.split('.')))
        diff = abs(len(version1) - len(version2))

        if diff > 0:
            if len(version1) > len(version2):
                for _ in range(diff):
                    version2.append(0)
            if len(version1) < len(version2):
                for _ in range(diff):
                    version1.append(0)

        for v1, v2 in zip(version1, version2):
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0