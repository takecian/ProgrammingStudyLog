# https://abc032.contest.atcoder.jp/tasks/abc032_c
# TLE

N, K = map(int, input().split())

S = [int(input()) for _ in range(N)]

if 0 in S:
    print(len(S))
    exit(0)

if min(S) > K:
    print(0)
    exit(0)

left = 0
right = 0
answer = 0
res = 1

while left < N and right < N:
    if res <= K:
        answer = max(answer, right - left)
        res *= S[right]
        right += 1
    else:
        res /= S[left]
        left += 1
        if res <= K:
            answer = max(answer, right - left)

if res <= K:
    answer = max(answer, right - left)

print(answer)