# https://atcoder.jp/contests/abc088/tasks/abc088_b?lang=ja

N = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

alice_score = 0
bob_score = 0

for i in range(len(a)):
    if i % 2 == 0:
        alice_score += a[i]
    else:
        bob_score += a[i]

print(alice_score - bob_score)
