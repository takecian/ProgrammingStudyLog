import sys

class Solution:
    def removeDuplicates(self, nums):
        i = 0
        p = -123
        while i < len(nums):
            if p != nums[i]:
                p = nums[i]
                i += 1
            else:
                del nums[i]
        return len(nums)

s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))