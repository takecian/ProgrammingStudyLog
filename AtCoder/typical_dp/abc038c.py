# https://beta.atcoder.jp/contests/abc038/tasks/abc038_c

N = int(input())
A = list(map(int, input().split()))

# print(A)

left = 0
right = 0
answer = 0
prev = 0

while left < N and right < N:
    if prev < A[right]:
        prev = A[right]
        right += 1
    else:
        diff = right - left
        answer += diff * (diff + 1) // 2

        left = right
        prev = 0

diff = right - left
answer += diff * (diff + 1) // 2

print(answer)
