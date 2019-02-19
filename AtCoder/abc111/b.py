# https://atcoder.jp/contests/abc111/tasks/abc111_b

N = int(input())

i = 1
while True:
    v = i * 100 + i * 10 + i
    if N <= v:
        print(v)
        break
    i += 1


