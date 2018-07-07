# https://beta.atcoder.jp/contests/abc102/tasks/abc102_b


N = int(input())

a = list(map(int, input().split()))

mini = 10**9
maxi = 1
for i in a:
    if i < mini:
        mini = i
    if maxi < i:
        maxi = i

print(maxi - mini)

