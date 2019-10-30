def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
	dp = [10**10] * (n + 1)
	dp[0] = 0
	for coin in denoms:
		for i in range(n+1):
			if coin <= i:
				dp[i] = min(dp[i], dp[i-coin] + 1)
	return dp[-1] if dp[-1] != 10**10 else -1
