# https://atcoder.jp/contests/abc126/tasks/abc126_d
import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N = int(input())

    ans = [-1] * (N + 1)
    vec = defaultdict(list)
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        vec[u].append((v, w))
        vec[v].append((u, w))

    que = [1]
    ans[1] = 0  # 1 を白にする

    while que:
        cursor = que.pop(0)
        for next, weight in vec[cursor]:
            if ans[next] == -1:
                if weight % 2 == 0:
                    ans[next] = ans[cursor]
                else:
                    ans[next] = 1 if ans[cursor] == 0 else 0
                que.append(next)
    for i in ans[1:]:
        print(i)


if __name__ == '__main__':
    main()
