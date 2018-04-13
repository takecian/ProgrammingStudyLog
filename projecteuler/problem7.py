
import sys

i = 8
prime_numbers = [2, 3, 5, 7]


def is_prime(number):
    res = list(filter(lambda x: number % x == 0, prime_numbers))
    return len(res) == 0


while i < sys.maxsize:
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        i += 1
        continue

    if is_prime(i):
        prime_numbers.append(i)
        print("prime found!: " + str(i) + ", " + str(len(prime_numbers)))
    i += 1
    if len(prime_numbers) == 10001:
        print(prime_numbers[-1])
        exit(0)
