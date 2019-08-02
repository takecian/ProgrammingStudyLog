class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        next_start = (None, None)
        l = 0
        in_sub = set()
        ans = 0
        for i in range(len(s)):
            if s[i] in in_sub:
                if next_start[0] != s[i]:
                    next_start = (s[i], i)
            else:
                if len(in_sub) < 2:
                    next_start = (s[i], i)
                    in_sub.add(s[i])
                else:
                    in_sub.clear()
                    in_sub.add(next_start[0])
                    l = next_start[1]

                    in_sub.add(s[i])
                    next_start = (s[i], i)
            ans = max(ans, i - l + 1)

        return ans


