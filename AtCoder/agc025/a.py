# https://agc025.contest.atcoder.jp/tasks/agc025_a

N = int(input())

if N < 10:
    print(N)
    exit(0)


r = str(N)[1:]
if int(r) == 0:
    print(sum(map(int, list(str(N // 2)))) * 2)
    exit(0)


l = sum(map(int, list(str(N))))


print(l)
