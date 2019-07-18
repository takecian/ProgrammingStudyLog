class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = 0
        a_c = 0
        b = 1
        b_c = 0
        for n in nums:
            if a == n:
                a_c += 1
            elif b == n:
                b_c += 1
            elif a_c == 0:
                a = n
                a_c = 1
            elif b_c == 0:
                b = n
                b_c = 1
            else:
                a_c -= 1
                b_c -= 1
        ans = []
        if nums.count(a) > len(nums) // 3:
            ans.append(a)
        if nums.count(b) > len(nums) // 3:
            ans.append(b)
        return ans
