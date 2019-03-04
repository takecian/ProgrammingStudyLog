# https://atcoder.jp/contests/abc120/tasks/abc120_b

import itertools
import collections
import bisect

def main():
    A, B, K = map(int, input().split())
    count = 0
    for i in range(max(A, B) + 1, 0, -1):
        # print(i)
        if A % i == 0 and B % i == 0:
            count += 1
            # print(i)
            if count == K:
                print(i)
                exit()

if __name__ == '__main__':
    main()
