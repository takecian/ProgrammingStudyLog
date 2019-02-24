# https://atcoder.jp/contests/abc119/tasks/abc119_b


def main():
    btc = 380000
    N = int(input())
    total = 0
    for _ in range(N):
        a, b = input().split()
        if b == "JPY":
            total += float(a)
        else:
            total += (float(a) * btc)
    print(total)

if __name__ == '__main__':
    main()