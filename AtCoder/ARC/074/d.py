# https://atcoder.jp/contests/arc074/tasks/arc074_b

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    n = int(input())
    al = list(map(int, input().split()))

    # front
    front = []
    front_sum = 0
    for i in range(n):
        front_sum += al[i]
        heappush(front, al[i])

    front_sums = [front_sum]
    for i in range(n, n * 2):
        minimum = heappop(front)
        if minimum < al[i]:
            front_sum += al[i] - minimum
            heappush(front, al[i])
        else:
            heappush(front, minimum)
        front_sums.append(front_sum)

    # back
    back = []
    back_sum = 0
    for i in range(n * 2, n * 3):
        back_sum += al[i]
        heappush(back, -al[i])

    back_sums = [back_sum]
    for i in range(n * 2 - 1, n - 1, -1):
        maximum = -heappop(back)
        if maximum > al[i]:
            back_sum += al[i] - maximum
            heappush(back, -al[i])
        else:
            heappush(back, -maximum)
        back_sums.append(back_sum)

    back_sums.reverse()

    # print(front_sums)
    # print(back_sums)

    ans = -10**20
    for f, b in zip(front_sums, back_sums):
        ans = max(ans, f - b)

    print(ans)


if __name__ == '__main__':
    main()
