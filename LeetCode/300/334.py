class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        lis = []
        for n in nums:
            pos = bisect.bisect_left(lis, n)
            if pos == len(lis):
                lis.append(n)
            else:
                lis[pos] = n
        return len(lis) > 2
