# https://leetcode.com/problems/regular-expression-matching/


class Solution:
    def isMatch(self, s, p):
        if len(p) == 0:
            return len(s) == 0

        is_first_matched = len(s) > 0 and p[0] in { s[0], "." }
        if len(p) >= 2 and p[1] == "*":
            return (self.isMatch(s, p[2:])) or (is_first_matched and self.isMatch(s[1:], p))
        else:
            return is_first_matched and self.isMatch(s[1:], p[1:])


s = Solution()
print(s.isMatch("aabc", "c*a*b"))

