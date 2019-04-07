# https://atcoder.jp/contests/abc123/tasks/abc123_c

import itertools
import collections
import bisect
import math

def main():
    N = int(input())
    last = N
    q = []
    for i in range(5):
        s = int(input())
        v = min(last, s)
        q.append(v)
        last = v

    f_step = math.ceil(N / q[0])
    ans = f_step
    # print(q)
    # print("ans = {}".format(ans))
    for i in range(1, 5):
        if q[i] < q[i-1]:
            # print("math.ceil(q[i] / q[i-1]) = {}".format(math.ceil(float(q[i]) / float(q[i-1]))))
            ans += math.ceil(N / q[i]) - 1
        else:
            ans += 1
        # print("ans = {}".format(ans))

    print(ans)


if __name__ == '__main__':
    main()
