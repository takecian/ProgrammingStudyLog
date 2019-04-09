# https://atcoder.jp/contests/abc071/tasks/arc081_a

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N = int(input())
    A = list(map(int, input().split()))

    c = Counter(A)
    a = 0
    b = 0
    c = sorted(c.items(), key=lambda i: i[0], reverse=True)
    # print(c)
    for item in c:
        # print(item)
        if a == 0:
            if item[1] >= 4:
                a = item[0]
                b = item[0]
                break
            elif item[1] >= 2:
                a = item[0]
        else:
            if item[1] >= 2:
                b = item[0]
                break
    print(a * b)


if __name__ == '__main__':
    main()
