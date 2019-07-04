class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cursor = m + n - 1
        n1_cursor = m - 1
        n2_cursor = n - 1
        while cursor >= 0:
            if n1_cursor < 0:
                nums1[cursor] = nums2[n2_cursor]
                cursor -= 1
                n2_cursor -= 1
            elif n2_cursor < 0:
                # no need to edit more
                break
            else:
                if nums1[n1_cursor] > nums2[n2_cursor]:
                    nums1[cursor] = nums1[n1_cursor]
                    cursor -= 1
                    n1_cursor -= 1
                else:
                    nums1[cursor] = nums2[n2_cursor]
                    cursor -= 1
                    n2_cursor -= 1
        return

