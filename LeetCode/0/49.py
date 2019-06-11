# https://leetcode.com/problems/group-anagrams/

import itertools
import collections
import bisect
import sys
input = sys.stdin.readline


class Solution:
    def groupAnagrams(self, strs):
        dic = {}
        for str in strs:
            str_sorted = ''.join(sorted(str))
            if str_sorted in dic:
                dic[str_sorted].append(str)
            else:
                dic[str_sorted] = [str]
        return [v for k, v in dic.items()]

def main():
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


if __name__ == '__main__':
    main()
