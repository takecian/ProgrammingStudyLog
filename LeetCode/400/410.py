class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l = max(nums)
        r = sum(nums)
        target = m

        ans = r
        while l <= r:
            mid = (l + r) // 2
            count = 1
            total = 0
            for num in nums:
                if total + num > mid:
                    count += 1
                    total = num
                else:
                    total += num
            # print(l, r, mid, count, target)
            if count <= target:
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        return ans