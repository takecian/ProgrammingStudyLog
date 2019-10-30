def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    target_array = [0, 0, 0] + array
    for i in range(3, len(target_array)):
        target_array[i] = target_array[i] + max(target_array[i - 3], target_array[i - 2])

    return max(target_array[-2], target_array[-1])
