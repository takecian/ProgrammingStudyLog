class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        n = len(s)
        dp = [False] * n
        for i in range(n):
            for word in dict:
                if s[i:i + len(word)] == word:
                    for j in range(i, i + len(word)):
                        dp[j] = True
        print(dp)
        ans = ''
        is_bold = False
        for i in range(n):
            if dp[i] and not is_bold:
                ans += '<b>'
                is_bold = True
            elif not dp[i] and is_bold:
                ans += '</b>'
                is_bold = False
            ans += s[i]
        if is_bold:
            ans += '</b>'

        return ans