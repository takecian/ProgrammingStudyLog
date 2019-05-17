import itertools
from collections import Counter
from collections import defaultdict
import bisect

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def main():
    n = int(input())
    for _ in range(n):
        i = int(input())
        if is_prime(i):
            print('Prime')
        else:
            print('Not prime')


if __name__ == '__main__':
    main()
