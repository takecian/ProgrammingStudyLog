# https://projecteuler.net/problem=33


def get_fractions():
    ns = []
    ds = []

    for d in range(10, 100):
        if d % 10 == 0:
            continue
        for n in range(10, d):
            f1 = n / d
            f2 = 0
            if int(n/10) == int(d%10):
                f2 = int(n%10) / int(d/10)
            elif int(n%10) == int(d/10):
                f2 = int(n / 10) / int(d % 10)

            if f2 != 0 and f1 == f2:
                print("n = " + str(n) + ",d = " + str(d) + ", " + str(f1) + " == " + str(f2))
                ns.append(n)
                ds.append(d)
    return (ns, ds)


def get_primes(v):
    m = {}
    i = 2

    while i <= v:
        while v % i == 0:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
            v //= i

        i += 1

    return m


def grouping_primes(l):
    dic = {}
    for d in l:
        s = get_primes(d)

        for key, value in s.items():
            if key in dic:
                dic[key] = value + dic[key]
            else:
                dic[key] = value
    return dic


ns, ds = get_fractions()

print(ns)  # [16, 26, 19, 49]
print(ds)  # [64, 65, 95, 98]

n_dic = grouping_primes(ns)
d_dic = grouping_primes(ds)

print(n_dic)
print(d_dic)

for key, value in n_dic.items():
    if key in d_dic:
        d_dic[key] = d_dic[key] - value if d_dic[key] > value else 0

print(d_dic)

ans = 1
for key, value in d_dic.items():
    ans *= key ** value

print(ans)