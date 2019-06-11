# https://leetcode.com/problems/count-and-say/

import itertools
from collections import Counter
import bisect


class Solution:
    def countAndSay(self, n):
        ans = '1'
        if n == 1:
            return ans
        while n > 1:
            temp = list(ans)
            next = ''
            current = temp[0]
            count = 1
            for a in temp[1:]:
                if current != a:
                    next += "{}{}".format(count, current)
                    current = a
                    count = 1
                else:
                    count += 1
            next += "{}{}".format(count, current)
            temp = next
            ans = temp
            n -= 1

        return ans


def main():
    s = Solution()
    for i in range(1,10):
        print(s.countAndSay(i))

if __name__ == '__main__':
    main()
