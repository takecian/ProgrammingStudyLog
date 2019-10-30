def subarraySort(array):
    # Write your code here.
    sorted_array = sorted(array)
    min_index = 10 ** 10
    max_index = 0
    for i in range(len(array)):
        if array[i] != sorted_array[i]:
            min_index = min(min_index, i)
            max_index = max(min_index, i)

    if max_index == 0 and min_index == 10 ** 10:
        return [-1, -1]
    else:
        return [min_index, max_index]