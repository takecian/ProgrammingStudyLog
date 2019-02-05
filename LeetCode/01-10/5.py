# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def isPalindrome(self, s):
        return s == s[::-1]

    def longestPalindrome(self, s):
        answer = ""
        for i in range(len(s)):
            for j in range(i + len(answer), len(s) + 1):
                # print(s[i:j])
                if self.isPalindrome(s[i:j]) and len(s[i:j]) > len(answer):
                    answer = s[i:j]

        return answer

# longestPalindrome("babad")
# print(longestPalindrome("aaddaa"))