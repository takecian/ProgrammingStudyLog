#
import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))

    ans = 1
    pos = [0] * (N + 1)
    for i in range(N):
        pos[i + 1] = pos[i] + L[i]
        if pos[i + 1] <= X:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
