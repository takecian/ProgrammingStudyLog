# https://atcoder.jp/contests/abc107/tasks/abc107_b

def main():
    H, W = map(int, input().split())
    a = [list(input()) for _ in range(H)]

    a = [ai for ai in a if any(ais == '#' for ais in ai)]

    i = 0
    while i < len(a[0]):
        if all(ai[i] == '.' for ai in a):
            for ai in a:
                del ai[i]
        else:
            i += 1
            continue

    for ai in a:
        print(''.join(ai))


if __name__ == '__main__':
    main()

 = [list(input()) for _ in range()]