# https://atcoder.jp/contests/diverta2019/tasks/diverta2019_b
import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    R, G, B, N = map(int, input().split())

    ans = 0
    for r in range(3001):
        rest = N - r * R
        if rest < 0:
            break
        for g in range(3001):
            rest_2 = rest - g * G
            if rest_2 >= 0 and rest_2 % B == 0:
                ans += 1
                # print('r {}, g {}, b {}'.format(r, g, rest // B))
    print(ans)


if __name__ == '__main__':
    main()
