# https://leetcode.com/problems/remove-element/


class Solution:
    def removeElement(self, nums, val):
        i = 0
        while i < len(nums):
            if val == nums[i]:
                del nums[i]
            else:
                i += 1
        return len(nums)

s = Solution()
print(s.removeElement([3,2,2,3], 3))