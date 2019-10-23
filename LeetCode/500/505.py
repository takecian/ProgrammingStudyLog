import heapq


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        if not maze or not maze[0]:
            return -1

        H = len(maze)
        W = len(maze[0])
        inf = 10 ** 15
        distances = [[inf] * W for _ in range(H)]
        distances[start[0]][start[1]] = 0

        que = []
        heapq.heappush(que, (0, start[0], start[1]))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while que:
            distance, h, w = heapq.heappop(que)
            if h == destination[0] and w == destination[1]:
                return distance

            for dh, dw in directions:
                next_h = h
                next_w = w
                while 0 <= next_w + dw < W and 0 <= next_h + dh < H and maze[next_h + dh][next_w + dw] != 1:
                    next_w += dw
                    next_h += dh

                dist = abs(w - next_w) + abs(h - next_h)
                if distance + dist < distances[next_h][next_w]:
                    distances[next_h][next_w] = distance + dist
                    heapq.heappush(que, (distances[next_h][next_w], next_h, next_w))

        return -1

