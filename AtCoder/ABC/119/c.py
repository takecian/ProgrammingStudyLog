# https://atcoder.jp/contests/abc119/tasks/abc119_c
import copy

def solve(t, l, c):
    # 長さ t の竹を L から少ないコストで作る方法を探す
    min_cost = 100000
    cand = []

    ptn = 1 << len(l)
    # print(l)
    # print("ptn = {}".format(ptn))
    for i in range(1, ptn):
        answers = []
        for j in range(0, len(l)):
            if (i >> j) & 1:
                answers.append(l[j])
        temp_cost = abs(t - sum(answers)) + (10 * (len(answers) - 1) if len(answers) > 1 else 0)
        if temp_cost < min_cost:
            min_cost = temp_cost
            cand = answers

    # print("cand = {}".format(cand))
    for d in cand:
        del l[l.index(d)]
    return min_cost, l


def main():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in range(N)]
    L.sort()

    answer = 1000000
    for targets in [[A, B, C], [A, C, B], [B, A, C], [B, C, A], [C, B, A], [C, A, B]]:
        is_done = [False] * 3
        L2 = copy.copy(L)
        total_cost = 0
        for i in range(len(targets)):
            if targets[i] in L2:
                del L2[L2.index(targets[i])]
                is_done[i] = True

        for i in range(3):
            if is_done[i]:
                continue

            # i の竹を L から少ないコストで作る方法を探す
            # print("try target = {}".format(targets[i]))
            cost, L2 = solve(targets[i], L2, 0)
            # print("cost = {}".format(cost))
            total_cost += cost

        answer = min(answer, total_cost)

    print(answer)


if __name__ == '__main__':
    main()
