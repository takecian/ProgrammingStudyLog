# https://atcoder.jp/contests/abc103/tasks/abc103_b

S = input()
T = input()

for _ in range(len(S)):
    if S == T:
        print("Yes")
        exit()
    S = S[-1] + S[0:len(S)-1]

print("No")
