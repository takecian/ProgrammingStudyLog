class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.solve('', n * 2, 0, 0)

    def solve(self, ptn, n, o, c):
        ans = []
        if n == o + c:
            return [ptn]
        if o > c:
            if o < n // 2:
                ans += self.solve(ptn + '(', n, o + 1, c)
            ans += self.solve(ptn + ')', n, o, c + 1)
        else:
            ans += self.solve(ptn + '(', n, o + 1, c)

        return ans