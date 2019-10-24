class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sets1 = set(nums1)
        sets2 = set(nums2)

        ans = []
        for s1 in sets1:
            if s1 in sets2:
                ans.append(s1)

        return ans
