class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        return self.rec(n, n)

    def rec(self, n, m):
        if n == 0:
            return ['']
        if n == 1:
            return ['0', '1', '8']

        insides = self.rec(n - 2, m)

        vals = []

        for content in insides:
            if n != m:
                vals.append('0' + content + '0')

            vals.append('1' + content + '1')
            vals.append('6' + content + '9')
            vals.append('9' + content + '6')
            vals.append('8' + content + '8')

        return vals