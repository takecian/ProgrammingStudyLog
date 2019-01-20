# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        answer = 0
        l = 0
        r = len(height) - 1
        while l < r:
            answer = max(answer, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return answer


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
