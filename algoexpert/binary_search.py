def binarySearch(array, target):
    # Write your code here.
    l = 0
    r = len(array)
    while l <= r:
        m = (l + r) // 2
        if array[m] == target:
            return m
        if array[m] < target:
            l = m + 1
        else:
            r = m - 1

    return -1