import heapq


class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        if len(forest) == 0:
            return 0

        h = len(forest)
        w = len(forest[0])

        heap = []
        for i in range(h):
            for j in range(w):
                if forest[i][j] > 1:
                    heapq.heappush(heap, (forest[i][j], i, j))

        def bfs(sh, sw, gh, gw):
            visit = [[False] * w for _ in range(h)]

            que = [(sh, sw, 0)]
            visit[sh][sw] = True

            while que:
                i, j, dis = que.pop(0)
                # print('{}, {}'.format(i,j))
                if i == gh and j == gw:
                    return dis

                for dh, dw in zip([0, 1, -1, 0], [1, 0, 0, -1]):
                    nh = i + dh
                    nw = j + dw
                    if 0 <= nw < w and 0 <= nh < h and forest[nh][nw] > 0 and visit[nh][nw] == False:
                        que.append((nh, nw, dis + 1))
                        visit[nh][nw] = True
                        # print(visit)

            return -1

        ans = 0
        sh = 0
        sw = 0
        while heap:
            height, i, j = heapq.heappop(heap)
            distance = bfs(sh, sw, i, j)
            # print('{}, {}, {}, {}, dis = {}'.format(sh, sw, i, j, distance))
            if distance == -1:
                return -1
            else:
                ans += distance
            sh = i
            sw = j

        return ans

