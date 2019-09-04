class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l <= r:
            m = (l + r) // 2
            # print('{} {} {}'.format(l, r, m))
            result = guess(m)
            if result == 0:
                return m
            elif result == 1:  # m is higher
                l = m + 1
            else:  # m is lower
                r = m - 1