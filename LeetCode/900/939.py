class Solution(object):
    def minAreaRect(self, points):
        seen = set()
        res = float('inf')
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    res = min(res, abs(x1 - x2) * abs(y1 - y2))

            seen.add((x1, y1))
        return res if res < float('inf') else 0