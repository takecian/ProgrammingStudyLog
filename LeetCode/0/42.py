class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        right_max = [0] * n
        left_max = [0] * n

        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i - 1])

        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i + 1])

        print(left_max)
        print(right_max)
        print(height)

        ans = 0
        for i in range(len(height)):
            ans += max(0, min(left_max[i], right_max[i]) - height[i])

        return ans

