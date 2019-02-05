# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        m = len(nums1)
        n = len(nums2)
        if  m  > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        imin = 0
        imax = m
        half_len = int((m + n + 1) / 2)

        while imin <= imax:
            i = int((imin + imax) / 2)
            j = half_len - i
            if i < m and nums2[j - 1] > nums1[i]:
                # imin is small, need to increase
                imin += 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # imax is big, need to decrease
                imax -= 1
            else:

                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])
                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0

s = Solution()
print(s.findMedianSortedArrays([1, 2], [1, 2]))
