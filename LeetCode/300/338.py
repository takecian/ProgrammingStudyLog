class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]

        loop = 1
        dp = [0] * (num + 1)
        dp[0] = 0
        dp[1] = 1
        while True:
            count = 0
            for i in range(2 ** loop, 2 ** (loop + 1)):
                if i > num:
                    return dp
                dp[i] = 1 + dp[count]
                count += 1
            loop += 1
