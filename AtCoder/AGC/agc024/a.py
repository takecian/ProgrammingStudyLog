# https://agc024.contest.atcoder.jp/tasks/agc024_a


A, B, C, K = map(int, input().split())

if K < 2:
    for i in range(K):
        A, B, C = B + C, A + C, A + B
    ans = A - B

    if ans > 10 ** 18:
        print('Unfair')
    else:
        print(ans)
else:
    if K % 2 == 0:
        ans = A - B
    else:
        ans = -A + B

    if ans > 10 ** 18:
        print('Unfair')
    else:
        print(ans)
