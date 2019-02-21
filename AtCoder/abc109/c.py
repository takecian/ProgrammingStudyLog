# https://atcoder.jp/contests/abc109/tasks/abc109_c

def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)


def main():
    N, X = map(int, input().split())

    xl = list(map(int, input().split()))

    ans = abs(X - xl[0])
    for i in range(1, len(xl)):
        ans = gcd(max(ans, abs(X - xl[i])), min(ans, abs(X - xl[i])))

    print(ans)


main()
