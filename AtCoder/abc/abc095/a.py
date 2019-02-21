# https://beta.atcoder.jp/contests/abc095/tasks/abc095_a

order = list(input())

price = 700

for o in order:
    if o == 'o':
        price += 100

print(price)