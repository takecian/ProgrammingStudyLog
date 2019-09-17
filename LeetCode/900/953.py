class Solution(object):
    def isAlienSorted(self, words, order):
        def lexcographcal(w1, w2, order):
            for c1, c2 in zip(w1,w2):
                if order.index(c1) < order.index(c2):
                    return True
                elif order.index(c1) > order.index(c2):
                    return False
            return len(w1) <= len(w2)

        for i in range(len(words)-1):
            if not lexcographcal(words[i], words[i+1], order):
                return False
        return True