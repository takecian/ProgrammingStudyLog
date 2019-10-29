def twoNumberSum(array, targetSum):
    # Write your code here.
    exist_vals = set()
    for num in array:
        expected = targetSum - num
        if expected in exist_vals:
            return [min(num, expected), max(num, expected)]
        exist_vals.add(num)
    return []
