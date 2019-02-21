# https://atcoder.jp/contests/abc117/tasks/abc117_b

N = int(input())
L = sorted(list(map(int, input().split())))

l_sum = sum(L[:len(L)-1])
longest = L[len(L)-1]

if l_sum > longest:
    print("Yes")
else:
    print("No")
