# https://atcoder.jp/contests/agc027/tasks/agc027_a


def main():
    N, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    count = 0
    i = 0
    while x > 0 and i < N:
        if a[i] <= x:
            count += 1
            x -= a[i]
        else:
            break
        i += 1

    if i == N and x != 0:
        count = max(0, count - 1)

    print(count)


if __name__ == '__main__':
    main()
