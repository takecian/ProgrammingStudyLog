# https://tdpc.contest.atcoder.jp/tasks/tdpc_game

A, B = map(int, input().split())

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

dp = [[0 for y in range(B + 1)] for x in range(A + 1)]

