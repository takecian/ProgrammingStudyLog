class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        n = len(colors)
        not_found = 10 ** 10
        distances = [[not_found, not_found, not_found] for _ in range(n)]

        for i in range(len(colors)):
            distances[i][colors[i] - 1] = 0

        for i in range(1, n):
            for j in range(3):
                distances[i][j] = min(distances[i][j], distances[i - 1][j] + 1)

        for i in range(n - 2, -1, -1):
            for j in range(3):
                distances[i][j] = min(distances[i][j], distances[i + 1][j] + 1)

        ans = []
        for i, v in queries:
            ans.append(distances[i][v - 1] if distances[i][v - 1] != not_found else -1)
        return ans