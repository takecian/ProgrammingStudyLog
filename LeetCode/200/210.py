import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop


class Solution:
    def findOrder(self, numCourses, prerequisites):
        dic = defaultdict(lambda: [])

        for c, p in prerequisites:
            dic[c].append(p)

        dones = set()
        ans = []
        for i in range(numCourses):
            if len(dic[i]) == 0:  # no prerequisites
                dones.add(i)
                ans.append(i)
                continue

        for i in range(numCourses):
            if i not in dones:
                candidates = [i]
                que = [i]

                can_do = True
                while que and can_do:
                    c = que.pop()
                    prereq = dic[c]

                    for p in prereq:
                        if p in dones:
                            continue

                        if p not in candidates:
                            candidates.append(p)
                            que.append(p)
                        else:
                            can_do = False
                            break
                if can_do:
                    candidates.reverse()
                    for c in candidates:
                        dones.add(c)
                        ans.append(c)
                else:
                    break

        print(ans)
        return ans if len(ans) == numCourses else []


def main():
    s = Solution()
    print(s.findOrder(2, [[1,0]]))
    print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
    print(s.findOrder(7, [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]))


if __name__ == '__main__':
    main()
