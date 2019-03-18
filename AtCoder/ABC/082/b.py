# https://atcoder.jp/contests/abc082/tasks/abc082_b

import itertools
import collections
import bisect

def main():
    s = input()
    t = input()
    s = ''.join(sorted(s))
    t = ''.join(sorted(t, reverse=True))
    # print(s)
    # print(t)
    print("Yes" if s < t else "No")



if __name__ == '__main__':
    main()
