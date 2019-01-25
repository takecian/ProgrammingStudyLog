# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        answer = 0
        ss = s

        symbols = [('IV', 4), ('IX', 9), ('XL', 40), ('XC', 90), ('CD', 400), ('CM', 900)]
        for symbol in symbols:
            if symbol[0] in ss:
                answer += symbol[1]
                ss = ss.replace(symbol[0], '')

        for c in ss:
            if c == 'I':
                answer += 1
            elif c == 'V':
                answer += 5
            elif c == 'X':
                answer += 10
            elif c == 'L':
                answer += 50
            elif c == 'C':
                answer += 100
            elif c == 'D':
                answer += 500
            elif c == 'M':
                answer += 1000

        return answer


s = Solution()
print(s.romanToInt("LVIII"))
