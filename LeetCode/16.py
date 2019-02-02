# https://leetcode.com/problems/3sum-closest/
import sys

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        print(nums)
        N, candidates = len(nums), []
        target_diff = sys.maxsize
        for i in range(N - 2):
            c1 = nums[i]
            l = i + 1
            r = N - 1
            current_diff = sys.maxsize
            while l < r:
                c2 = nums[l]
                c3 = nums[r]
                total = c1 + c2 + c3
                diff = abs(target - total)
                # print('{}+{}+{}= {}, diff = {}'.format(c1, c2, c3, total, current_diff))
                if diff < current_diff:
                    current_diff = diff
                    if current_diff < target_diff:
                        target_diff = current_diff
                        candidates = [c1, c2, c3]
                if total < target:
                    l += 1
                else:
                    r -= 1

        return sum(candidates)


s = Solution()
print(s.threeSumClosest([-5, -5, -4, 0, 0, 3, 3, 4, 5], -2))
# print(s.threeSumClosest([-1, 2, 1, -4], 1))
# print(s.threeSumClosest([1, 1, 1, 0], -100))
