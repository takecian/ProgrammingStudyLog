# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        N, result = len(nums), []
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:  # すでに調べた数字ならスキップ
                continue
            target = nums[i]*-1
            s, e = i+1, N-1  # 一つ前と後から挟んでいく
            while s < e:
                if nums[s]+nums[e] == target:
                    result.append([nums[i], nums[s], nums[e]])
                    s = s+1
                    while s < e and nums[s] == nums[s-1]:
                        s = s+1
                elif nums[s] + nums[e] < target:
                    s = s+1
                else:
                    e = e-1
        return result


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))


# import itertools
# TLE
# class Solution:
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         answers = []
#         for l in list(itertools.combinations(nums, 3)):
#             if sum(l) == 0:
#                 l = tuple(sorted(l))
#                 if l not in answers:
#                     answers.append(l)
#         return answers
