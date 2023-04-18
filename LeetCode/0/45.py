class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        inf = 1e10
        steps = [inf for _ in range(n)]
        steps[0] = 0
        for i in range(n):
            for step in range(1, nums[i]+1):
                next_pos = i + step
                if next_pos < n:
                    steps[next_pos] = min(steps[next_pos], steps[i] + 1)
        
        return steps[-1]
