def waterArea(heights):
    # Write your code here.
    n = len(heights)
    left_heights = [0] * n
    right_heights = [0] * n

    for i in range(1, n):
        left_heights[i] = max(left_heights[i - 1], heights[i - 1])
    for i in range(n - 2, -1, -1):
        right_heights[i] = max(right_heights[i + 1], heights[i + 1])

    ans = 0
    for i in range(n):
        pillar_height = min(right_heights[i], left_heights[i])
        ans += max(0, pillar_height - heights[i])
    return ans
