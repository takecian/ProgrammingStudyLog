# https://atcoder.jp/contests/abc080/tasks/abc080_b

import itertools
import collections
import bisect

def main():
    N = int(input())
    s = sum(map(int, list(str(N))))
    print("Yes" if N % s == 0 else "No")

if __name__ == '__main__':
    main()
