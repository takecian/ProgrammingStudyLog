X = int(input())

m = 0
for b in range(1, 100):
    for p in range(2, 20):
        val = b ** p
        if val > 1000:
            continue
        if m < val <= X:
            m = val
        # print(val)

print(m)
