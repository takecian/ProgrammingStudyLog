class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0,n,2):
            if i == n-1:
                return nums[i]
            if nums[i] != nums[i+1]:
                return nums[i]