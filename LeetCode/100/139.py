class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(dp)):
            if dp[i]:
                sub_str = s[i:]
                for w in wordDict:
                    if sub_str.find(w) == 0:
                        dp[i + len(w)] = True

        return dp[-1]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            if dp[i]:
                rest = s[i:]
                for w in wordDict:
                    if rest.startswith(w):
                        dp[i + len(w)] = True
        return dp[-1]
