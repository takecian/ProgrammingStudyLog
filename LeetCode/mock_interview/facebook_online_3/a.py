class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        i = 0
        while i < len(s):
            val = dic[s[i]]
            ans += val

            if val == 5 or val == 10:
                if i > 0 and dic[s[i - 1]] == 1:
                    ans -= 2
            elif val == 50 or val == 100:
                if i > 0 and dic[s[i - 1]] == 10:
                    ans -= 20
            elif val == 500 or val == 1000:
                if i > 0 and dic[s[i - 1]] == 100:
                    ans -= 200
            i += 1
        return ans
