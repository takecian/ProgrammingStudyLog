# https://atcoder.jp/contests/abc081/tasks/abc081_b

import itertools
import collections
import bisect

# 素因数分解
def prime_dic(n):
    ans = 0

    while n % 2 == 0:
        ans += 1
        n //= 2

    return ans

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = list(map(lambda x: prime_dic(x), A))
    print(min(A))

if __name__ == '__main__':
    main()
