
import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    n = int(input())

    ans = len(str(n))
    i = 1
    while i * i <= n:
        if n % i == 0:
            a = i
            b = n // i
            ans = min(ans, max(len(str(a)), len(str(b))))

        i += 1

    print(ans)

if __name__ == '__main__':
    main()
