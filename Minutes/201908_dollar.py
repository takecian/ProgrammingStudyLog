#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    d = list(str(int(input())))
    d.reverse()
    ans = []
    for i in range(len(d)):
        if i != 0 and i % 3 == 0:
            ans.append(',')
        ans.append(d[i])
    ans.append('$')
    ans.reverse()
    print(''.join(ans))


if __name__ == '__main__':
    main()
