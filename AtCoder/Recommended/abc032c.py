# https://abc032.contest.atcoder.jp/tasks/abc032_c
# TLE

N, K = map(int, input().split())

S = [int(input()) for _ in range(N)]

if 0 in S:
    print(len(S))
    exit(0)

answer = 0

for left in range(N):
    temp = 1
    right = left
    while right < N:
        temp *= S[right]
        if temp > K:
            if right - left > answer:
                answer = right - left
            break
        right += 1

    if right - left > answer:
        answer = right - left

print(answer)