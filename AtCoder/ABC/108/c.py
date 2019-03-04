# https://atcoder.jp/contests/abc108/tasks/arc102_a

N, K = map(int, input().split())

ans = 0
if K % 2 == 0:
    # 余りが 全部 0 か全部 K//2 である数字の組み合わせ
    c1 = len([i for i in range(K, N + 1, K)])
    ans += c1 * c1 * c1
    c2 = len([i for i in range(K // 2, N + 1, K)])
    ans += c2 * c2 * c2
else:
    # 余りが 全部 K//2 である数字の組み合わせ
    c1 = len([i for i in range(K, N + 1, K)])
    ans += c1 * c1 * c1

print(ans)
