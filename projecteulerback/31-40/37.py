# https://projecteuler.net/problem=37


def is_prime(n):
    if 2 > n: return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


def left_to_right(n):
    l = str(n)
    if len(l) < 2: return 0
    l = l[1:]

    v = 0
    i = 0
    for d in l[::-1]:
        v += int(d) * 10 ** i
        i += 1
    return v


def right_to_left(n):
    l = str(n)
    if len(l) < 2: return 0
    l = l[:-1]

    v = 0
    i = 0
    for d in l[::-1]:
        v += int(d) * 10 ** i
        i += 1
    return v


bp = []

for i in range(20,1000000):
    if i % 10 == 1:
        continue

    v = i
    # print("start = " + str(i))

    both_prime = True

    while is_prime(v):
        v = left_to_right(v)
        # print(v)
    if v != 0:
        both_prime = False
    # else:
    #     print(str(i) + " is prime. left_to_right")


    v = i
    while is_prime(v):
        v = right_to_left(v)
        # print(v)
    if v != 0:
        both_prime = False
    # else:
    #     print(str(i) + " is prime. right_to_left")

    if both_prime:
        print(str(i) + " is prime both!!!!")
        bp.append(i)

        if len(bp) == 11:
            break

print(sum(bp))