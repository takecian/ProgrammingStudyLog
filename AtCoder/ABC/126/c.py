# https://atcoder.jp/contests/abc126/tasks/abc126_c
import itertools
from collections import Counter
from collections import defaultdict
import bisect
import math

def main():
    N, K = map(int, input().split())

    ans = 0.0
    if N < K:
        for i in range(1, N + 1):
            x = math.ceil(math.log2(K / i))
            # print(x)
            ans += (1 / min(N, K)) * 0.5 ** x
    else:
        ans += (N - K + 1) / N
        for i in range(1, K):
            x = math.ceil(math.log2(K / i))
            # print(x)
            ans += (1 / N) * 0.5 ** x

    print(ans)

if __name__ == '__main__':
    main()
