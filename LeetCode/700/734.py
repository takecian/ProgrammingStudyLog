from collections import defaultdict


class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False

        pair_list = defaultdict(list)
        for p1, p2 in pairs:
            pair_list[p1].append(p2)
            pair_list[p2].append(p1)

        print(pair_list)
        for w1, w2 in zip(words1, words2):
            print(w1, w2)
            if w1 == w2:
                continue
            if w1 in pair_list[w2]:
                continue
            return False
        return True
