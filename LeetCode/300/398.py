class Solution:

    def __init__(self, nums: List[int]):
        self.nums = [(v, i) for i, v in enumerate(nums)]
        self.values = nums

        self.nums.sort(key=lambda vi: vi[0])
        self.values.sort()
        # print(self.nums)

    def pick(self, target: int) -> int:
        # print(self.values)
        left = bisect.bisect_left(self.values, target)
        right = bisect.bisect_right(self.values, target) - 1
        # print(left,right)
        return self.nums[random.randint(left, right)][1]