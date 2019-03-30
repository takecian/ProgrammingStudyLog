# https://atcoder.jp/contests/exawizards2019/tasks/exawizards2019_a

import itertools
import collections
import bisect

def main():
    A, B, C = map(int, input().split())
    print("Yes" if A == B and B == C else "No")

if __name__ == '__main__':
    main()
