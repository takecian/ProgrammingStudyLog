def productSum(array):
    # Write your code here.
    def calc_sum(arr, level):
        ans = 0
        for ele in arr:
            if type(ele) is int:
                ans += ele
            else:
                ans += (level + 1) * calc_sum(ele, level + 1)
        return ans

    return calc_sum(array, 1)
