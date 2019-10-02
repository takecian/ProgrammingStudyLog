class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palaindrome(text):
            return text == text[::-1]

        if is_palaindrome(s):
            return True

        l = 0
        r = len(s) - 1
        skip = 0
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                break
        candidate1 = s[:l] + s[l + 1:]
        candidate2 = s[:r] + s[r + 1:]

        if is_palaindrome(candidate1) or is_palaindrome(candidate2):
            return True
        return False
