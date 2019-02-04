# https://atcoder.jp/contests/abc051/tasks/abc051_b

K, S = map(int, input().split())


answer = 0
for x in range(K + 1):
    for y in range(K + 1):
        z = S - x - y
        if 0 <= z <= K:
            answer += 1

print(answer)
