# https://leetcode.com/problems/flood-fill/
from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        que = deque()
        target_color = image[sr][sc]
        # print(image)
        que.append((sr, sc))

        r_size = len(image)
        c_size = len(image[0])
        visited = [[False] * c_size for _ in range(r_size)]

        while que:
            r, c = que.popleft()
            image[r][c] = newColor
            for dc, dr in zip([0, 1, 0, -1], [1, 0, -1, 0]):
                neigbor_c = c + dc
                neigbor_r = r + dr
                if 0 <= neigbor_c < c_size and 0 <= neigbor_r < r_size:
                    if not visited[neigbor_r][neigbor_c] and image[neigbor_r][neigbor_c] == target_color:
                        image[neigbor_r][neigbor_c] = newColor
                        que.append((neigbor_r, neigbor_c))
                        visited[neigbor_r][neigbor_c] = True

        return image