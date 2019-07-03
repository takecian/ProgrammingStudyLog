from collections import defaultdict
from collections import deque


class Solution:
    def gardenNoAdj(self, N, paths):
        answers = [0] * N
        edges = defaultdict(list)
        for path in paths:
            edges[path[0] - 1].append(path[1] - 1)
            edges[path[1] - 1].append(path[0] - 1)

        for i in range(N):
            if answers[i] != 0:
                continue

            candidate_plants = [1, 2, 3, 4]
            for neibor_garden in edges[i]:
                if answers[neibor_garden] in candidate_plants:
                    candidate_plants.remove(answers[neibor_garden])
            answers[i] = candidate_plants[0]

        return answers


def main():
    s = Solution()
    # print(s.gardenNoAdj(3, [[1,2],[2,3],[3,1]]))
    # print(s.gardenNoAdj(4, [[1,2],[3,4]]))
    # print(s.gardenNoAdj(4, [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]))
    # print(s.gardenNoAdj(5, [[4,1],[4,2],[4,3],[2,5],[1,2],[1,5]]))
    print(s.gardenNoAdj(10, [[5,8],[10,7],[3,6],[9,6],[10,8],[9,4],[5,2],[1,2],[8,7],[4,3]]))

if __name__ == '__main__':
    main()
