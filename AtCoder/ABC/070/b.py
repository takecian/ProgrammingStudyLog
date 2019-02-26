# https://atcoder.jp/contests/abc070/tasks/abc070_b

def main():
    A, B, C, D = map(int, input().split())
    print(max(0, min(B, D) - max(A, C)))


if __name__ == '__main__':
    main()
