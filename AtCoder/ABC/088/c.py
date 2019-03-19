# https://atcoder.jp/contests/abc088/tasks/abc088_c

import itertools
import collections
import bisect

def main():
    A = [list(map(int, input().split())) for _ in range(3)]

    for a1 in range(101):
        b1 = A[0][0] - a1
        b2 = A[0][1] - a1
        b3 = A[0][2] - a1
        for a2 in range(101):
            if all([a2 + b1 == A[1][0], a2 + b2 == A[1][1], a2 + b3 == A[1][2]]):
                for a3 in range(101):
                    if all([a3 + b1 == A[2][0], a3 + b2 == A[2][1], a3 + b3 == A[2][2]]):
                        print("Yes")
                        exit()

    print("No")


if __name__ == '__main__':
    main()
