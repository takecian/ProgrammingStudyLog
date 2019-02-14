# https://atcoder.jp/contests/abc114/tasks/abc114_b


S = list(map(int, list(input())))

ans = 999

for i in range(len(S)-2):
    v = S[i] * 100 + S[i+1] * 10 + S[i+2]
    # print(v)
    ans = min(ans, abs(753-v))

print(ans)
