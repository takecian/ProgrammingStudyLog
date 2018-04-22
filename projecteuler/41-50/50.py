# https://projecteuler.net/problem=50
#
# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?


def is_prime(n):
    if 2 > n: return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


d = []
for i in range(5000):
    if is_prime(i):
        d.append(i)


i = 0
max_cons = 0

for i in range(len(d)):
    # print(d[i])
    total = d[i]  # is prime

    for j in range(i+1, len(d)):
        total += d[j]
        # print("================= i = " + str(i) + ", j = " + str(j) + ", total = " + str(total))
        # print(total)
        if is_prime(total) and total < 1000000:
            cons = j - i + 1
            if cons > max_cons:
                print("i = " + str(i) + ", j = " + str(j) + ", cons = " + str(cons) + ", total = " + str(total))
                max_cons = cons
    # break

print(max_cons)
# total = 0
# for i in range(22):
#     total += d[i]
#     print(total)