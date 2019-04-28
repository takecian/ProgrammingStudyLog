# https://atcoder.jp/contests/abc125/tasks/abc125_b

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        ans += (V[i] - C[i]) if V[i] - C[i] > 0 else 0
    print(ans)

if __name__ == '__main__':
    main()
