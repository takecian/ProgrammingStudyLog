# https://projecteuler.net/problem=45


p_dic = {}
h_dic = {}


def calc_pentagonal(n):
    v = n * (3 * n - 1) // 2
    p_dic[v] = True


def calc_hexagonal(n):
    v = n * (2 * n - 1)
    h_dic[v] = True


def ret_triagle(n):
    return n * (n + 1) // 2


# calculate numbers in advance
for i in range(1, 100000):
    calc_pentagonal(i)
    calc_hexagonal(i)


for i in range(286, 100000):
    v = ret_triagle(i)
    if v in p_dic and v in h_dic:
        print("found, i = " + str(i) + ", value = " + str(v))
        break



