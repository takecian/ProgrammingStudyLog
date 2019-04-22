# https://leetcode.com/problems/plus-one/

import itertools
import collections
import bisect


class Solution:
    def plusOne(self, digits):
        number = int(''.join(list(map(str, digits))))
        number += 1
        return list(map(int, list(str(number))))

def main():
    s = Solution()
    print(s.plusOne([4,3,2,1]))

if __name__ == '__main__':
    main()
