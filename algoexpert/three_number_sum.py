def threeNumberSum(array, targetSum):
    # Write your code here.
    ans = []
    n = len(array)
    array.sort()
    for i in range(n - 2):
        target = targetSum - array[i]
        l = i + 1
        r = n - 1
        while l < r:
            if array[l] + array[r] == target:
                ans.append([array[i], array[l], array[r]])
                l += 1
                r -= 1
            elif array[l] + array[r] < target:
                l += 1
            else:
                r -= 1
    return ans
