import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    a = list(input())
    b = list(input())

    ans = 0
    current = 0

    for i in range(len(b)):
        if a[i] == b[i]:
            current += 1

    if current % 2 == 0:
        ans += 1

    for i in range(1, len(a) - len(b) + 1):
        if a[i - 1] == b[i - 1]:
            current -= 1

        if a[i + len(b) - 1] == b[i + len(b) - 1]:
            current += 1

        if current % 2 == 0:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
