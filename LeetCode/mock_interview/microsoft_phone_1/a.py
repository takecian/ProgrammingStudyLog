class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        alpha_str = ''.join(list(filter(lambda c: c.isalpha(), S)))[::-1]
        ans = ''
        i = 0
        for c in S:
            if c.isalpha():
                ans += alpha_str[i]
                i += 1
            else:
                ans += c
        return ans