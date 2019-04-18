# https://atcoder.jp/contests/abc069/tasks/abc069_b

import itertools
import collections
import bisect

def main():
    s = input()
    print(s[0] + str(len(s[1:-1])) + s[-1])

if __name__ == '__main__':
    main()

