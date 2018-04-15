
def permutation(n):
    if n < 2: return 1
    return n * permutation(n - 1)


millionth = 100*10000

c = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

rest = millionth

while rest > 0 and c:
    # print(c)
    i = 0
    while c:
        p = permutation(len(c) - 1)
        if rest <= p:
            print(str(c[i]) + ", " + str(rest))
            c.pop(i)
            break

        rest -= p
        i += 1

print(c)