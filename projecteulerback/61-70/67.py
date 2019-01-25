# https://projecteuler.net/problem=67

data = open("p067_triangle.txt", "r")

lines = data.readlines()

data.close()


rows = []

for line in lines:
    rows.append(list(map(int, line.split())))


# calculate max total from bottom
for r in range(98, -1, -1):
    for i in range(len(rows[r])):
        if rows[r+1][i] > rows[r+1][i+1]:
            rows[r][i] += rows[r+1][i]
        else:
            rows[r][i] += rows[r+1][i+1]

print(rows[0][0])
