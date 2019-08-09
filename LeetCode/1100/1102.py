import heapq

class Solution:
    def maximumMinimumPath(self, matrix: List[List[int]]) -> int:
        R = len(matrix)
        C = len(matrix[0])

        q = [(-matrix[0][0], 0, 0)]  # get maximum value

        visited = [[False] * C for _ in range(R)]
        while q:
            t, r, c = heapq.heappop(q)
            if r == R - 1 and c == C - 1:
                return -t
            for dr, dc in zip([-1,0,1,0],[0,-1,0,1]):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(q, (max(t, -matrix[nr][nc]), nr, nc))

