# https://atcoder.jp/contests/exawizards2019/tasks/exawizards2019_b

import itertools
import collections
import bisect

def main():
    N = int(input())
    S = list(input())
    print("Yes" if S.count('R') > S.count('B') else "No")

if __name__ == '__main__':
    main()
