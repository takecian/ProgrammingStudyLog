from collections import defaultdict


class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False

        pair_list = defaultdict(list)
        for p1, p2 in pairs:
            pair_list[p1].append(p2)
            pair_list[p2].append(p1)

        def is_similar(w1, w2):
            que = [w1]
            visited = set([w1])

            while que:
                next_que = []
                while que:
                    word = que.pop()
                    if word == w2:
                        return True
                    for next_word in pair_list[word]:
                        if next_word not in visited:
                            next_que.append(next_word)
                            visited.add(next_word)

                que = next_que
            print(w1, w2)
            return False

        for w1, w2 in zip(words1, words2):
            # print(w1,w2)
            if w1 == w2:
                continue
            if is_similar(w1, w2):
                continue
            return False
        return True