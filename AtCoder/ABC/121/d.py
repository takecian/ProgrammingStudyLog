# https://atcoder.jp/contests/abc121/tasks/abc121_d

def calc(x):
    if x % 2:  # 奇数なら 1 or 0
        if x % 4 == 1:
            return 1
        else:
            return 0
    else:
        if x % 4 == 0:
            return x
        else:
            return x ^ 1

def main():
    A, B = map(int, input().split())
    ans = calc(B) ^ calc(max(0, A-1))
    print(ans)

if __name__ == '__main__':
    main()
