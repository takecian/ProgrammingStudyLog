# https://leetcode.com/problems/4sum/


class Solution:
    def fourSum_2n(self, nums, target):
        ptn = 1 << len(nums)
        answers = []
        for i in range(ptn):
            if format(i, 'b').count("1") != 4:
                continue
            ans = []
            for j in range(len(nums)):
                if (i >> j) & 1:
                    ans.append(nums[j])
            # print(ans)
            ans.sort()
            if sum(ans) == target and ans not in answers:
                answers.append(ans)
        return answers

    def fourSum(self, nums, target):
        nums.sort()
        answers = []
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    ans = [nums[i], nums[j], nums[l], nums[r]]
                    if sum(ans) == target:
                        ans.sort()
                        if ans not in answers:
                            answers.append(ans)
                        r -= 1
                    else:
                        if sum(ans) > target:
                            r -= 1
                        else:
                            l += 1
        return answers

s = Solution()
print(s.fourSum([1,-2,-5,-4,-3,3,3,5], -11))
