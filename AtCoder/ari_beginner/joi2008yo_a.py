
i = int(input())

p = 1000 - i
count = 0
while p > 0:
    if p >= 500:
        p -= 500
        count += 1
    elif p >= 100:
        p -= 100
        count += 1
    elif p >= 50:
        p -= 50
        count += 1
    elif p >= 10:
        p -= 10
        count += 1
    elif p >= 5:
        p -= 5
        count += 1
    elif p >= 1:
        p -= 1
        count += 1

print(count)

