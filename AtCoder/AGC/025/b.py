# https://atcoder.jp/contests/agc025/tasks/agc025_b


def main():
    N, A, B, K = map(int, input().split())

    if K == 0:
        print(1)
        exit()

    combi_cache = [0] * (N + 1)
    combi_cache[1] = N
    for i in range(2, N+1):
        combi_cache[i] = combi_cache[i-1] * (N-i+1) // i

    ans = 0
    for a in range(N+1):
        n = K - a * A
        if n < 0:  # これ以上はやる意味ない
            break
        if n % B == 0:
            ans += (combi_cache[a] * combi_cache[n // B]) % 998244353

    print(ans)


if __name__ == '__main__':
    main()
