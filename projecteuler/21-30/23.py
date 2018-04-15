# https://projecteuler.net/problem=23
#
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


def get_prime_divisors_sum(n):
    d = [1]
    i = 2

    while i * i <= n:
        if n % i == 0:
            d.append(i)
            if i != n / i:
                d.append(int(n / i))
        i += 1

    return sum(d)


a = []
for i in range(2, 28124): # 28124
    if i < get_prime_divisors_sum(i):
        # print(str(i) + " is adundant.")
        a.append(i)

print(len(a))
total = 0

redundant_li = []
for i in a:
    for j in a:
        if i + j < 28124:
            redundant_li.append(i + j)

redundant_li = list(set(redundant_li))

all_li = list(range(1,28124))

total = sum(all_li) - sum(redundant_li)


print(total)