# https://leetcode.com/problems/string-to-integer-atoi/submissions/

class Solution:
    def is_int(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        can_accept_sign = True
        is_positive = True
        answer = 0
        for c in str:
            if can_accept_sign:
                if c == ' ' and answer == 0:
                    continue
                if c == '+' and answer == 0:
                    can_accept_sign = False
                    continue
                if c == '-' and answer == 0:
                    can_accept_sign = False
                    is_positive = False
                    continue

            can_accept_sign = False
            if self.is_int(c):
                answer *= 10
                answer += int(c)
            else:
                break

        if is_positive:
            return min(2**31 - 1, answer)
        else:
            return max(-2**31, -answer)


s = Solution()
print(s.myAtoi(" -42"))
