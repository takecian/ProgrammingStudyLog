class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def create_subsets(ans, index):
            if index == len(nums):
                return ans

            next_ans = []
            for a in ans:
                next_ans.append(a)
                next_ans.append(a + [nums[index]])
            return create_subsets(next_ans, index + 1)

        return create_subsets([[]], 0)
