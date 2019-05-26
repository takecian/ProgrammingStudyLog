# https://atcoder.jp/contests/abc128/tasks/abc128_d

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N, K = map(int, input().split())
    D = list(map(int, input().split()))

    ans = 0
    print(D)
    for i in range(K+1):
        front_k = i
        back_k = K - i
        index = min(i, N)
        back_index = max(index, N - back_k)
        print('{}, {}'.format(D[:index], D[back_index:]))

        front = D[:index]
        front.sort()
        front_max = 0
        for j in range(front_k):
            front_max = max(front_max, sum(front[j:]))

        back = D[back_index:]
        back.sort()
        back_max = 0
        for j in range(back_k):
            back_max = max(back_max, sum(back[j:]))

        print('front = {}, back = {}'.format(front_max, back_max))

        ans = max(ans, front_max + back_max)

    print(ans)


if __name__ == '__main__':
    main()
