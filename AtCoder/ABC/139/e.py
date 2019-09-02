#
import sys
from collections import deque

def input(): return sys.stdin.readline().strip()

def main():
    n = int(input())
    agrid = []
    agrid_pointer = [0] * n

    for i in range(n):
        al = list(map(int, input().split()))
        for j in range(len(al)):
            al[j] -= 1
        agrid.append(al)

    ans = 0

    def find_next(idx, q, m):
        if agrid_pointer[idx] == n - 1 or i in m:  # もう全部対戦済み or この日対戦済み
            return

        target = agrid[idx][agrid_pointer[idx]]
        if agrid_pointer[target] == n - 1 or target in m:  # もう全部対戦済み or この日対戦済み
            return

        if agrid[target][agrid_pointer[target]] != idx:
            return

        q.append((idx, target))
        m.add(idx)
        m.add(target)

    que = deque()
    first_matching = set()
    for i in range(n):
        find_next(i, que, first_matching)

    while que:
        ans += 1

        changed = []
        #  試合を消化
        while que:
            i, j = que.popleft()
            agrid_pointer[i] += 1
            agrid_pointer[j] += 1
            changed.append(i)
            changed.append(j)

        #  試合が行われた選手に対して次の試合をマッチングする
        next_que = deque()
        match = set()
        for i in changed:
            find_next(i, next_que, match)

        # print(match)
        que = next_que

    # print(aconditions)
    # 対戦が残ってたら
    for p in agrid_pointer:
        if p != n - 1:
            print(-1)
            return
    print(ans)


if __name__ == '__main__':
    main()
