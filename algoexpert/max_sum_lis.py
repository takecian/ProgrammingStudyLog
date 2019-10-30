
def maxSumIncreasingSubsequence(array):
    prevs = [None] * len(array)
    sums = array[:]
    max_index = 0
    for i in range(len(array)):
        current_num = array[i]
        for j in range(i):
            prev_num = array[j]
            if prev_num < current_num and sums[j] + current_num > sums[i]:
                sums[i] = sums[j] + current_num
                prevs[i] = j
        if sums[i] > sums[max_index]:
            max_index = i

    def build_seq():
        seq = []
        index = max_index
        while index is not None:
            seq.append(array[index])
            index = prevs[index]
        seq.reverse()
        return seq

    return [sums[max_index], build_seq()]


print(maxSumIncreasingSubsequence([8,12,2,3,15,5,7]))

