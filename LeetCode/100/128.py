class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        num_set = set(nums)
        for n in num_set:
            if n - 1 in num_set:
                continue
            count = 1
            current = n
            while current + 1 in num_set:
                count += 1
                current += 1
            ans = max(ans, count)
        return ans