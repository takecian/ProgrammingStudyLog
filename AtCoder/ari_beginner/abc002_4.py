# https://atcoder.jp/contests/abc002/tasks/abc002_4

N, M = map(int, input().split())

relationship = [list(map(int, input().split())) for _ in range(M)]

# print(relationship)

answer = 1
for i in range(1 << N):
    r_map = [0 for _ in range(N)]
    # print(format(i, 'b'))
    for j in relationship:
        if ((i >> (j[0]-1)) & 1) and ((i >> (j[1]-1)) & 1):
            r_map[j[0]-1] += 1
            r_map[j[1]-1] += 1
    # print(r_map)
    r = []
    for m in range(N):
        if (i >> m) & 1:
            r.append(r_map[m])
    # print(r)
    if len(r) > 0 and min(r) == len(r) - 1:
        # print(format(i, 'b'))
        answer = max(answer, len(r))

print(answer)
