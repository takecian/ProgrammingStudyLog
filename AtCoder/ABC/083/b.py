# https://atcoder.jp/contests/abc083/tasks/abc083_b
import itertools
import collections
import bisect
import sys
input = sys.stdin.readline

def main():
    N, A, B = map(int, input().split())

    ans = 0
    for i in range(1, N+1):
        ans += i if A <= sum(map(int, list(str(i)))) <= B else 0
    print(ans)

if __name__ == '__main__':
    main()
