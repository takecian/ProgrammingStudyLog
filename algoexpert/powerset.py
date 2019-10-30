def powerset(array):
    # Write your code here.
    ans = [[]]
    for num in array:
        next_array = []
        for current in ans:
            next_array.append(current)
            next_array.append(current + [num])
        ans = next_array

    return ans
