memo = {}

class Solution(object):
    def getMoneyAmount(self, n):
        return self.calc(1, n)

    def calc(self, l, r):
        if l >= r:  # answer number, no cost
            return 0

        if (l, r) in memo:
            return memo[(l, r)]

        minres = 10 ** 15
        for i in range(l, r + 1):
            res = i + max(self.calc(l, i - 1), self.calc(i + 1, r))
            minres = min(res, minres)

        memo[(l, r)] = minres
        return memo[(l, r)]
