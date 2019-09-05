class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_and_index = {}
        for i in range(len(nums)):
            expected = target - nums[i]
            if expected in num_and_index:
                return [num_and_index[expected], i]

            num_and_index[nums[i]] = i

