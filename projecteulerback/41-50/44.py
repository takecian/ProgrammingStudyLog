# https://projecteuler.net/problem=44

cache = {}


def calc_pentagonal(n):
    if n in cache:
        return cache[n]
    cache[n] = n * (3 * n - 1) // 2
    return cache[n]


v_dic = {}


def is_pentagonal(n):
    return n in v_dic


length = 10000

# create dic to store pentagonal numbers
for i in range(length * 2):
    v_dic[calc_pentagonal(i)] = True


for k in range(2, length):
    for j in range(1, k):
        pk = calc_pentagonal(k)
        pj = calc_pentagonal(j)
        a = pk + pj
        s = pk - pj

        if is_pentagonal(a) and is_pentagonal(s):
            print("k = " + str(k) + ", j = " + str(j) + ", pk = " + str(pk) + ", pj = " + str(pj) + ", a = " + str(a) + ", s = " + str(s))
            print("answer = " + str(s))
            exit(0)



