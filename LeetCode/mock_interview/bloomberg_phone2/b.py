from collections import Counter
from collections import defaultdict


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        c = Counter(words)
        dic = defaultdict(list)

        most_frequent = c.most_common()[0][1]

        count = 0
        last_frequent = None
        for w, i in c.most_common():
            dic[i].append(w)
            count += 1
            if count == k:
                last_frequent = i
            if last_frequent and last_frequent != i:
                break

        ans = []

        i = most_frequent
        # print(dic)
        while len(ans) < k:
            dic[i].sort()
            while len(ans) < k and len(dic[i]) > 0:
                w = dic[i].pop(0)
                ans.append(w)
            i -= 1
            # print(ans)
        return ans