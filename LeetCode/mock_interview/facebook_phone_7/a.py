class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpa_num = ''
        for c in s:
            if c.isalnum():
                alpa_num += c.lower()
        return alpa_num == alpa_num[::-1]
