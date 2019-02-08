# https://leetcode.com/problems/longest-valid-parentheses/


class Solution:
    def longestValidParentheses(self, s):
        longest = 0
        current = 0
        left_counter = 0
        for c in s:
            if c == "(":
                left_counter += 1
            else: # ")"
                if left_counter > 0:
                    left_counter -= 1
                    current += 1
                    if left_counter == 0:
                        longest = max(current, longest)
                else:
                    current = 0

        return longest * 2

s = Solution()
print(s.longestValidParentheses("(()"))
