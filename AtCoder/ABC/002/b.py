# https://atcoder.jp/contests/abc002/tasks/abc002_2
import re
import itertools
import collections
import bisect
import sys
input = sys.stdin.readline

def main():
    W = input()
    ans = re.sub(r'[a|i|u|e|o]+', "", W).replace("\n", "")
    print(ans)

if __name__ == '__main__':
    main()
