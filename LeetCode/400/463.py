class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        H = len(grid)
        W = len(grid[0])

        def calc_perimeter(h, w):
            ret = 0
            for dh, dw in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
                nh = h + dh
                nw = w + dw
                if nh < 0 or H == nh or nw < 0 or W == nw:
                    ret += 1
                else:
                    if grid[nh][nw] == 0:
                        ret += 1
            return ret

        ans = 0
        for h in range(H):
            for w in range(W):
                if grid[h][w] == 0:
                    continue
                # land
                ans += calc_perimeter(h, w)
        return ans