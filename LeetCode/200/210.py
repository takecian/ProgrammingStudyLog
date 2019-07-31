from collections import defaultdict


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        predic = defaultdict(list)
        neigh = defaultdict(list)
        for c, p in prerequisites:
            predic[c].append(p)
            neigh[p].append(c)

        que = []
        for i in range(numCourses):
            if len(predic[i]) == 0:  # no prerequisites
                que.append(i)

        ans = []
        while que:
            node = que.pop()
            ans.append(node)  # take course

            for i in neigh[node]:
                predic[i].remove(node)
                if len(predic[i]) == 0:  # if ready to take
                    que.append(i)

        # print(ans)
        return ans if len(ans) == numCourses else []
