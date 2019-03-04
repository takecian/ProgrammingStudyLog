# https://abc100.contest.atcoder.jp/tasks/abc100_d
# NOTE: TLE

import operator


def get_ans(tup):
    return abs(tup[0]) + abs(tup[1]) + abs(tup[2])


def calc1(tup):
    return tup[0] + tup[1] + tup[2]

def calc2(tup):
    return tup[0] + tup[1] - tup[2]

def calc3(tup):
    return tup[0] - tup[1] + tup[2]

def calc4(tup):
    return tup[0] - tup[1] - tup[2]

def calc5(tup):
    return -tup[0] + tup[1] + tup[2]

def calc6(tup):
    return -tup[0] + tup[1] - tup[2]

def calc7(tup):
    return -tup[0] - tup[1] + tup[2]

def calc8(tup):
    return -tup[0] - tup[1] - tup[2]


def knapsack(num, weight, value, func):
    inf = 100000000000
    dp = [[-inf for i in range(weight + 1)] for j in range(num + 1)]

    for i in range(weight + 1):
        dp[0][i] = (0, 0, 0)

    # DP
    for i in range(num):
        for w in range(weight + 1):
            if 0 < w:  # dp[i][w-weight[i]の状態にi番目の荷物が入る可能性がある
                if func(tuple(map(operator.add, dp[i][w - 1], value[i]))) > func(dp[i][w]):
                    dp[i + 1][w] = tuple(map(operator.add, dp[i][w - 1], value[i]))
                else:
                    dp[i + 1][w] = dp[i][w]
            else:  # 入る可能性はない
                dp[i + 1][w] = dp[i][w]

    return dp[num][weight]


N, M = map(int, input().split())

cakes = []
for i in range(N):
    cakes.append(tuple(map(int, input().split())))

# print(cakes)

print(
    max(
        get_ans(knapsack(N, M, cakes, calc1)),
        get_ans(knapsack(N, M, cakes, calc2)),
        get_ans(knapsack(N, M, cakes, calc3)),
        get_ans(knapsack(N, M, cakes, calc4)),
        get_ans(knapsack(N, M, cakes, calc5)),
        get_ans(knapsack(N, M, cakes, calc6)),
        get_ans(knapsack(N, M, cakes, calc7)),
        get_ans(knapsack(N, M, cakes, calc8)),
    )
)
# print(knapsack(N, M, cakes, calc1))

# print(sum(knapsack(N, M, cakes, calc1)))
