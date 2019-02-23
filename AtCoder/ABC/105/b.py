# https://atcoder.jp/contests/abc105/tasks/abc105_b

def main():
    N = int(input())
    for i in range(N//4 + 1):
        for j in range(N // 7 + 1):
            if 4 * i + 7 * j == N:
                print("Yes")
                exit()
    print("No")


if __name__ == '__main__':
    main()


