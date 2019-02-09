# https://yahoo-procon2019-qual.contest.atcoder.jp/tasks/yahoo_procon2019_qual_a

N, K = map(int, input().split())

if K <= (N + 1) / 2:
    print("YES")
else:
    print("NO")
