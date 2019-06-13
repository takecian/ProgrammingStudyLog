import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

class Solution:
    def minWindow(self, s, t):
        ans = ''

        n = len(s)
        t_counter = Counter(t)
        counter = defaultdict(lambda: 0)
        covered = 0
        start = 0
        min_len = 10**10

        for i, c in enumerate(s):
            counter[c] += 1
            if c in t_counter and counter[c] == t_counter[c]:
                covered += 1
            while start < n:
                char = s[start]
                if char not in t or counter[char] > t_counter[char]:
                    # we can proceed
                    counter[char] -= 1
                    start += 1
                else:
                    break

            length = i - start + 1
            if covered == len(t_counter) and length < min_len:
                min_len = length
                ans = s[start:(i + 1)]
        return ans

def main():
    s = Solution()
    print(s.minWindow("a", "a"))

if __name__ == '__main__':
    main()
