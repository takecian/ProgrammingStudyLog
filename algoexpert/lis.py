def longestIncreasingSubsequence(array):
    # Write your code here.
    n = len(array)
    prev_index = [None] * n
    length = [1] * n
    max_length_index = 0
    for i in range(n):
        for j in range(0, i):
            if array[j] < array[i] and length[j] + 1 >= length[i]:
                prev_index[i] = j
                length[i] = length[j] + 1
        if length[i] >= length[max_length_index]:
            max_length_index = i

    # print(length)
    # print(prev_index, max_length_index)

    ans = []
    index = max_length_index
    while True:
        ans.append(array[index])
        index = prev_index[index]
        if index is None:
            break

    ans.reverse()
    return ans

print(longestIncreasingSubsequence([100,1,2,3,4,101]))
print(longestIncreasingSubsequence([-1]))
print(longestIncreasingSubsequence([1,5,-1,10]))
