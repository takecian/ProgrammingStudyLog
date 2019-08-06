class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        ans = ''
        S = S[::-1]
        for c in S:
            if c == '-':
                continue
            if len(ans) == K: # '2E9W'
                ans = '-' + ans
            elif len(ans) % (K+1) == K: # 'AAAA-2E9W'
                ans = '-' + ans
            if c.isdigit():
                ans = c + ans
            else:
                ans = c.upper() + ans
        return ans