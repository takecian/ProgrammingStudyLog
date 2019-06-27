import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop


class Solution:
    def findOrder(self, numCourses, prerequisites):
        dic = defaultdict(lambda: [])
        neigh = defaultdict(lambda: [])
        for c, p in prerequisites:
            dic[c].append(p)
            neigh[p].append(c)

        que = []
        for i in range(numCourses):
            if len(dic[i]) == 0:  # no prerequisites
                que.append(i)

        ans = []
        while que:
            node = que.pop()
            ans.append(node)

            for i in neigh[node]:
                dic[i].remove(node)
                if len(dic[i]) == 0:
                    que.append(i)

        # print(ans)
        return ans if len(ans) == numCourses else []


def main():
    s = Solution()
    print(s.findOrder(2, [[1,0]]))
    print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
    print(s.findOrder(7, [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]))


if __name__ == '__main__':
    main()
