# https://leetcode.com/problems/integer-to-roman/
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# the range from 1 to 3999.


class Solution:
    def one_int_to_roman(self, num, symbols):
        if num in [1,2,3]:
            return ''.join(symbols[0] * num)
        elif num in [6, 7, 8]:
            return symbols[1] + ''.join([symbols[0] * (num - 5)])
        elif num == 4:
            return symbols[0] + symbols[1]
        elif num == 5:
            return symbols[1]
        elif num == 9:
            return symbols[0] + symbols[2]
        return ''

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        one_symbols = ['I', 'V', 'X']
        two_symbols = ['X', 'L', 'C']
        three_symbols = ['C', 'D', 'M']
        four_symbols = ['M']

        nums = list(reversed(list(map(int, list(str(num))))))
        all_symbols = [one_symbols, two_symbols, three_symbols, four_symbols]

        answer = ''
        for n, s in zip(nums, all_symbols):
            answer = self.one_int_to_roman(n, s) + answer

        return answer



s = Solution()
print(s.intToRoman(58))

