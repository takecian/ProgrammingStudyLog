def getNthFib(n):
    # Write your code here.
    dp = [0] * n
    if n == 1:
        return 0
    if n == 2:
        return 1

    dp[0] = 0
    dp[1] = 1
    for i in range(2, n):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[n - 1]
