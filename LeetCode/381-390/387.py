# https://leetcode.com/problems/first-unique-character-in-a-string/

import itertools
import collections
import bisect
import sys
input = sys.stdin.readline


class Solution:
    def firstUniqChar(self, s):
        dic = {}
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1

        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i

        return -1


def main():
    s = Solution()
    print(s.firstUniqChar('loveleetcode'))


if __name__ == '__main__':
    main()
