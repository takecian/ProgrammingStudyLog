def kadanesAlgorithm(array):
    # Write your code here.
	ans = -1000
	val = 0
	for num in array:
		val = max(val, 0)
		val += num
		ans = max(ans, val)
	return ans
