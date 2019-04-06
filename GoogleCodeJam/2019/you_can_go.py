import itertools
import collections
import bisect

def main():
    N = int(input())
    for i in range(N):
        l = int(input())
        path = list(input())
        ans = []
        for p in path:
            ans.append('E' if p == 'S' else 'S')
        print("Case #{}: {}".format(i + 1, ''.join(ans)))

if __name__ == '__main__':
    main()
