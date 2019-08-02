
import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    n = int(input())
    sl = [input() for _ in range(n)]

    counter = [[0] * 26 for _ in range(n)]

    for i in range(n):
        for c in sl[i]:
            counter[i][ord(c) - ord('a')] += 1

    ans = ''
    for i, a in enumerate(zip(*counter)):
        ans += chr(ord('a') + i) * min(a)

    print(ans)

if __name__ == '__main__':
    main()
