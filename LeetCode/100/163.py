class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [lower-1] + nums + [upper+1]
        ranges = []
        for i in range(1,len(nums)):
            diff = nums[i] - nums[i-1] - 1
            start = nums[i-1]+1
            if diff == 1:
                ranges.append(str(start))
            elif diff > 1:
                ranges.append(str(start) + '->' + str(start + diff - 1))
        # print(nums)
        # print(diffs)
        return ranges