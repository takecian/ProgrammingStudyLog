# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """

        # find center
        m = 0
        l = 0
        r = mountain_arr.length() - 1
        while l <= r:
            m = (l + r + 1) // 2
            if mountain_arr.get(m - 1) < mountain_arr.get(m) > mountain_arr.get(m + 1):
                break
            elif mountain_arr.get(m - 1) < mountain_arr.get(m):
                l = m + 1
            else:
                r = m - 1
        # print(m)
        # find right side
        l = 0
        r = m
        while l <= r:
            c = (l + r) // 2
            if mountain_arr.get(c) == target:
                return c

            if mountain_arr.get(c) < target:
                l = c + 1
            else:
                r = c - 1
        # find left side
        l = m + 1
        r = mountain_arr.length() - 1
        while l <= r:
            c = (l + r) // 2
            if mountain_arr.get(c) == target:
                return c

            if mountain_arr.get(c) > target:
                l = c + 1
            else:
                r = c - 1

        return -1