# https://atcoder.jp/contests/abc119/tasks/abc119_c
import copy
import itertools


# 長さ t の竹を L から少ないコストで作る方法を探す
def solve(t, l, c):
    min_cost = 100000
    cand = []


    # 全組み合わせを考えて一番コストの低いものを使う
    ptn = 1 << len(l)  # Bit 全探索
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
    for targets in itertools.permutations([A, B, C]):
        is_done = [False] * 3
        L2 = copy.copy(L)
        total_cost = 0

        # 同じ長さの竹があったら使う
        for i in range(len(targets)):
            if targets[i] in L2:
                del L2[L2.index(targets[i])]
                is_done[i] = True

        # 同じ長さの竹がない場合
        for i in range(3):
            if is_done[i]:
                continue

            cost, L2 = solve(targets[i], L2, 0)
            total_cost += cost

        answer = min(answer, total_cost)

    print(answer)


if __name__ == '__main__':
    main()
