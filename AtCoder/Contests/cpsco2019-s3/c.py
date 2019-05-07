# https://atcoder.jp/contests/cpsco2019-s3/tasks/cpsco2019_s3_c

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N = int(input())
    s = [list(map(int, input().split())) for _ in range(N)]

    s.sort(key=lambda x: x[0])
    ans = 0
    current_end = 0
    for start, end in s:
        if current_end == 0:
            ans += 1
            current_end = end
        else:
            if start <= current_end:
                current_end = max(current_end, end)
            else:
                ans += 1
                current_end = end
    print(ans)


if __name__ == '__main__':
    main()
