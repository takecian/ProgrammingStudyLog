from collections import defaultdict
from collections import deque


class Solution:
    def gardenNoAdj(self, N, paths):

        candidate_plants = [[1, 2, 3, 4] for _ in range(N)]

        answers = [0] * N

        need_check = set()

        edges = defaultdict(list)
        for path in paths:
            edges[path[0] - 1].append(path[1] - 1)
            edges[path[1] - 1].append(path[0] - 1)
            need_check.add(path[0] - 1)
            need_check.add(path[1] - 1)

        que = deque()
        que.append(0)

        while len(que) > 0:
            garden = que.popleft()
            if answers[garden] == 0:
                plants = candidate_plants[garden]
                answers[garden] = plants[0]

                # print(candidate_plants)
                candidate_plants[garden] = [plants[0]]
                # print(candidate_plants)

                if garden in need_check:
                    need_check.remove(garden)

                for next_garden in edges[garden]:
                    if answers[next_garden] == 0:
                        # remove chosen plant from candidates
                        if answers[garden] in candidate_plants[next_garden]:
                            candidate_plants[next_garden].remove(answers[garden])
                        que.append(next_garden)

            if len(que) == 0:
                for i in range(N):
                    if i in need_check:
                        que.append(i)
                        break
            if len(need_check) == 0:
                break
            # print(que)

        for i in range(N):
            if answers[i] == 0:  # anything is okay
                answers[i] = 1

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
