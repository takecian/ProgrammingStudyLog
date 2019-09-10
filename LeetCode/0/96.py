class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}

        def solve(num):
            if num < 2:
                return 1
            if num == 2:
                return 2
            if num in memo:
                return memo[num]
            val = 0
            for left in range(num):
                right = num - 1 - left
                val += solve(left) * solve(right)
            memo[num] = val
            return memo[num]

        return solve(n)