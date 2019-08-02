
import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    n = int(input())
    a = list(map(int, input().split()))

    cumulative = 0
    count1 = 0
    for i in range(len(a)):
        cumulative += a[i]
        if i % 2 == 0: # positive
            if cumulative <= 0:
                count1 += abs(cumulative) + 1
                cumulative += (abs(cumulative) + 1)
        else:  # negative
            if cumulative >= 0:
                count1 += abs(cumulative) + 1
                cumulative -= (abs(cumulative) + 1)
        # print('count = {} c = {}'.format(count, cumulative))

    cumulative = 0
    count2 = 0
    for i in range(len(a)):
        cumulative += a[i]
        if i % 2 == 0: # negative
            if cumulative >= 0:
                count2 += abs(cumulative) + 1
                cumulative -= (abs(cumulative) + 1)
        else:  # positive
            if cumulative <= 0:
                count2 += abs(cumulative) + 1
                cumulative += (abs(cumulative) + 1)
        # print('count = {} c = {}'.format(count, cumulative))

    print(min(count1, count2))


if __name__ == '__main__':
    main()
