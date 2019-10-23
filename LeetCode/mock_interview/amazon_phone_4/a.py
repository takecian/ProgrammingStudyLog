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

        while que:
            distance, h, w = heapq.heappop(que)
            # left
            next_w = w
            cursor_w = w
            while 0 <= cursor_w:
                if maze[h][cursor_w] == 1:
                    break
                next_w = cursor_w
                cursor_w -= 1
            # print(h, next_w)
            if distances[h][w] + w - next_w < distances[h][next_w]:
                distances[h][next_w] = distances[h][w] + w - next_w
                heapq.heappush(que, (distance + w - next_w, h, next_w))

            # up
            next_h = h
            cursor_h = h
            while 0 <= cursor_h:
                if maze[cursor_h][w] == 1:
                    break
                next_h = cursor_h
                cursor_h -= 1
            # print(next_h, w)
            if distances[h][w] + h - next_h < distances[next_h][w]:
                distances[next_h][w] = distances[h][w] + h - next_h
                heapq.heappush(que, (distance + h - next_h, next_h, w))

            # right
            next_w = w
            cursor_w = w
            while cursor_w < W:
                if maze[h][cursor_w] == 1:
                    break
                next_w = cursor_w
                cursor_w += 1
            # print(h, next_w)
            if distances[h][w] + next_w - w < distances[h][next_w]:
                distances[h][next_w] = distances[h][w] + next_w - w
                heapq.heappush(que, (distance + next_w - w, h, next_w))

            # down
            next_h = h
            cursor_h = h
            while cursor_h < H:
                if maze[cursor_h][w] == 1:
                    break
                next_h = cursor_h
                cursor_h += 1
            # print(next_h, w)
            if distances[h][w] + next_h - h < distances[next_h][w]:
                distances[next_h][w] = distances[h][w] + next_h - h
                heapq.heappush(que, (distance + next_h - h, next_h, w))

        # for i in range(len(distances)):
        #     print(distances[i])
        return distances[destination[0]][destination[1]] if distances[destination[0]][destination[1]] != inf else -1

