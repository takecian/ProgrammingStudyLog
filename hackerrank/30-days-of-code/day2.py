import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    meal = float(input())
    tip = int(input())
    tax = int(input())
    print(round(meal + meal * tip / 100 + meal * tax / 100))

if __name__ == '__main__':
    main()
