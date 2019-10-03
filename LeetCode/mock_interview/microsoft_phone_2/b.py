class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for c in s:
            val = ord(c) - ord('A') + 1
            ans = ans * 26 + val
        return ans