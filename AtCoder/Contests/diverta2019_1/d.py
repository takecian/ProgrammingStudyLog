# https://atcoder.jp/contests/diverta2019/tasks/diverta2019_d
import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N = int(input())

    ans = 0
    i = 1
    while i * i <= N:
        if N % i == 0:
            candidates = [i - 1, N // i - 1]
            for c in candidates:
                if c > 0 and N // c == N % c:
                    ans += c
        i += 1

    print(ans)


if __name__ == '__main__':
    main()
