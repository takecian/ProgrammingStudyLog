class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find pivot
        n = len(nums)
        if n == 0:
            return -1

        l = 0
        r = n - 1
        while r - l > 1:
            m = (l + r) // 2
            if nums[l] < nums[m]:
                l = m

            if nums[m] < nums[r]:
                r = m
        # l is pivot
        # print(l, r)
        top = l
        down = r
        l = 0
        r = top
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            if nums[m] > target:
                r = m - 1
        l = down
        r = n - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            if nums[m] > target:
                r = m - 1
        return -1