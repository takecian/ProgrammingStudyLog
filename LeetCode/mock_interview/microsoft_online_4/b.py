from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        threshold = len(nums) // 3
        c = Counter(nums)
        ans = []
        for d, c in c.most_common():
            if c > threshold:
                ans.append(d)
            else:
                break
        return ans