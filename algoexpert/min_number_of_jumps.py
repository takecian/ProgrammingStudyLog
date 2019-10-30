def minNumberOfJumps(array):
    # Write your code here.
    steps = [10 ** 10] * len(array)
    steps[0] = 0

    for i in range(len(array)):
        for j in range(1, array[i] + 1):
            if i + j == len(array):
                break
            steps[i + j] = min(steps[i + j], steps[i] + 1)

    return steps[-1]

print(minNumberOfJumps([3,4,2,1,2,3,7,1,1,1,3]))
