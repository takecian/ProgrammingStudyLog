

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = collections.defaultdict(int)
        counter2 = collections.defaultdict(int)
        for n in nums1:
            counter1[n] += 1
        for n in nums2:
            counter2[n] += 1

        ans = []
        for k in counter1:
            m = min(counter1[k], counter2[k])
            for _ in range(m):
                ans.append(k)
        return ans