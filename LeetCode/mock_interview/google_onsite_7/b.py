from collections import defaultdict


class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def compress(word):
            l = []
            prev = None
            count = 0
            for c in word:
                if len(l) == 0:
                    l.append([c, 1])
                else:
                    if l[-1][0] == c:
                        l[-1][1] += 1
                    else:
                        l.append([c, 1])
            return l

        s_counter = compress(S)

        ans = 0
        for word in words:
            w_counter = compress(word)
            if len(s_counter) != len(w_counter):
                continue

            can_strech = True
            for (c1, l1), (c2, l2) in zip(s_counter, w_counter):
                if c1 != c2:
                    can_strech = False
                    break
                if l1 < 3 and l1 != l2:
                    can_strech = False
                    break
                if l1 < l2:
                    can_strech = False
                    break

            if can_strech:
                ans += 1
        return ans