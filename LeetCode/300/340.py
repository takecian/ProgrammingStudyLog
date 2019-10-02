class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counter = collections.defaultdict(int)

        def count_uniq():
            return len(list(filter(lambda c: counter[c] > 0, counter)))

        ans = 0
        b = 0
        e = 0
        while e < len(s):
            c = s[e]
            counter[c] += 1
            while count_uniq() > k:
                counter[s[b]] -= 1
                b += 1
            ans = max(ans, e - b + 1)
            e += 1

        return ans
