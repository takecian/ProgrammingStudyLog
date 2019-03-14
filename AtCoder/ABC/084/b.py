# https://atcoder.jp/contests/abc084/tasks/abc084_b

import itertools
import collections
import bisect

def main():
    A, B = map(int, input().split())
    S = input()

    try:
        fir = int(S[:A])
        sec = int(S[B:])
    except ValueError:
        print("No")
        exit()

    if S[A] == '-':
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
