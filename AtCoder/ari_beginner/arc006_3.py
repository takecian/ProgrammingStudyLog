# https://atcoder.jp/contests/arc006/tasks/arc006_3

N = int(input())
W = [int(input()) for _ in range(N)]

ds = []
for w in W:
    if len(ds) == 0:
        ds.append([w])
    else:
        i = 0
        while i < len(ds):
            if ds[i][-1] >= w:
                ds[i].append(w)
                break
            i += 1
        if i == len(ds):
            ds.append([w])

print(len(ds))

