from collections import defaultdict


def fourNumberSum(array, targetSum):
    # Write your code here.
    n = len(array)

    array.sort()
    pair_sums = defaultdict(list)
    ans = []

    for i in range(n - 1):
        for j in range(i + 1, n):
            diff = targetSum - array[i] - array[j]
            if diff in pair_sums:
                for a, b in pair_sums[diff]:
                    ans.append([a, b, array[i], array[j]])
        for k in range(i):
            current_sum = array[k] + array[i]
            pair_sums[current_sum].append((array[k], array[i]))


    return ans

print(fourNumberSum([7, 6, 4, -1, 1, 2], 16))
# print(fourNumberSum([1, 2, 3, 4, 5, 6, 7], 10))
# print(fourNumberSum([5, -5, -2, 2, 3, -3], 0))
