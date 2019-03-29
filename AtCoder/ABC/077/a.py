# https://atcoder.jp/contests/abc077/tasks/abc077_a

import itertools
import collections
import bisect

def main():
    c1 = input()
    c2 = input()
    c1r = ''.join(list(reversed(c1)))
    c2r = ''.join(list(reversed(c2)))
    print("YES" if c1 == c2r and c2 == c1r else "NO")

if __name__ == '__main__':
    main()
