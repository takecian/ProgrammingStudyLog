# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        i = len(nums) - 1
        while i > 0:
            if nums[i - 1] < nums[i]:
                break
            else:
                i -= 1
        if i == 0:
            nums.sort()
        else:
            j = len(nums) - 1
            k = i - 1  # find the last "ascending" position
            while nums[j] <= nums[k]:
                j -= 1
            nums[k], nums[j] = nums[j], nums[k]

            l, r = k + 1, len(nums) - 1  # reverse the second part
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        #     print(nums[i:len(nums)])
        # print(nums)
        return

s = Solution()
s.nextPermutation([1,3,2])
