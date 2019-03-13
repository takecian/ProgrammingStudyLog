# https://atcoder.jp/contests/aising2019/tasks/aising2019_a

N = int(input())
H = int(input())
W = int(input())

h_candidate = N - H + 1
w_candidate = N - W + 1

print(h_candidate * w_candidate)
