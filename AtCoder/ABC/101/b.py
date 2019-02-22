# https://atcoder.jp/contests/abc101/tasks/abc101_b

N = int(input())
Sn = sum(list(map(int, str(N))))

print("Yes" if N % Sn == 0 else "No")
