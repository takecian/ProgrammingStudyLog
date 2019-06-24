# https://leetcode.com/problems/course-schedule/

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop


class Solution:
    def canFinish(self, numCourses, prerequisites):

        dic = defaultdict(lambda: [])

        for c, p in prerequisites:
            dic[c].append(p)

        dones = set()
        for i in range(numCourses):
            if len(dic[i]) == 0:  # no prerequisites
                dones.add(i)
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
                    [dones.add(c) for c in candidates]
                else:
                    break

        return len(dones) == numCourses


def main():
    s = Solution()
    print(s.canFinish(2, [[1,0]]))
    print(s.canFinish(2, [[1,0],[0,1]]))

if __name__ == '__main__':
    main()
