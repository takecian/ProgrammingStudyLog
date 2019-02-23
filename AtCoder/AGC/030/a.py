# https://atcoder.jp/contests/agc030/tasks/agc030_a

def main():
    A, B, C = map(int, input().split())
    deli = 0
    if A > 0 and C > 0:
        eat = min(A, C)
        deli += eat
        A -= eat
        C -= eat

    # 美味しくないクッキーがなくなった, お腹壊してない
    if B > 0 and C > 0:
        eat = min(B, C)
        deli += eat * 2
        B -= eat
        C -= eat
    # お腹壊してない

    if C > 0:
        deli += 1

    deli += B
    print(deli)


if __name__ == '__main__':
    main()

