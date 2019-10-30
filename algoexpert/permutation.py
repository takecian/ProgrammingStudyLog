def getPermutations(array):
    # Write your code here.
    ans = []

    def rec(rest_array, current):
        nonlocal ans
        if len(rest_array) == 0:
            if len(current) > 0:
                ans.append(current)
            return

        for i in range(len(rest_array)):
            new_rest_array = rest_array[:i] + rest_array[i + 1:]
            rec(new_rest_array, current + [rest_array[i]])

    rec(array, [])
    return ans
