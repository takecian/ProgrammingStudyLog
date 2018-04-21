# https://projecteuler.net/problem=47
# This code shows answer but it takes a few minutes.

def get_prime_dic(n):
    p = {}

    i = 2
    while i <= n:
        while n % i == 0:
            if i in p:
                p[i] += 1
            else:
                p[i] = 1
            n //= i
        i += 1

    return p


i = 0
while True:
    if i % 10000 == 0:
        print(i)
    if len(get_prime_dic(i)) != 4:
        i += 1
        continue
    if len(get_prime_dic(i+1)) != 4:
        i += 2
        continue
    if len(get_prime_dic(i+2)) != 4:
        i += 3
        continue

    print("three = " + str(i))
    if len(get_prime_dic(i + 3)) != 4:
        i += 4
        continue

    print("four consecutive intergers starts from " + str(i))
    break


# for i in range(1000,100000):
    # print(get_prime_dic(i))
