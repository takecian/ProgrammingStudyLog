class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = [0] * len(nums)
        if len(nums) == 0:
            return -1
        left_sum[0] = nums[0]
        for i in range(len(nums) - 1):
            left_sum[i + 1] = nums[i + 1] + left_sum[i]

        right_sum = [0] * len(nums)
        reveresed_nums = list(reversed(nums))
        right_sum[0] = reveresed_nums[0]
        for i in range(len(reveresed_nums) - 1):
            right_sum[i + 1] = reveresed_nums[i + 1] + right_sum[i]

        print(left_sum)
        right_sum.reverse()
        print(right_sum)
        for i in range(len(nums)):
            if i == 0:
                if right_sum[1] == 0:
                    return 0
                continue

            if i == len(nums) - 1:
                if left_sum[i - 1] == 0:
                    return i
                continue

            if left_sum[i - 1] == right_sum[i + 1]:
                return i

        return -1