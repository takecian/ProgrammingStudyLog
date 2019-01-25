def conv(c):
    return ord(c) - ord("A") + 1


def calculate(n):
    l = list(map(conv, list(n)))
    return sum(l)


file = open("p022_names.txt", "r")
names = list(file.read().split(","))
file.close()

names = list(map(lambda x: x.replace("\"", ""), names))


names = sorted(names)

total_score = 0
for i, n in enumerate(names):
    val = calculate(n) * (i + 1)
    total_score += val

print(total_score)

