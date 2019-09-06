class Solution:
    def numSquares(self, n: int) -> int:
        candidate = []
        i = 1
        while i * i <= n:
            candidate.append(i*i)
            i += 1
        cnt = 0
        to_check = {n}
        while to_check:
            cnt += 1
            next_check = set()
            for x in to_check:
                for y in candidate:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    next_check.add(x-y)
            to_check = next_check

        return cnt