# https://leetcode.com/problems/divide-two-integers/

class Solution:
    def divide(self, dividend: 'int', divisor: 'int') -> 'int':
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)

        ans = 0
        while dividend_abs >= divisor_abs:
            shift = 1
            val = divisor_abs
            while dividend_abs >= val:
                ans += shift
                dividend_abs -= val

                shift <<= 1
                val <<= 1

        if (dividend < 0 and divisor < 0) or (dividend >= 0 and divisor >= 0):
            return min(ans, 2**31 - 1)
        else:
            return -min(ans, 2**31)

