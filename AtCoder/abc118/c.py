# https://atcoder.jp/contests/abc118/tasks/abc118_c

def main():
    N = int(input())
    A = list(map(int, input().split()))  # 体力

    while True:
        A.sort()

        before_min = A[0]
        after_min = before_min
        for i in range(1, N):
            A[i] = (A[i] % A[0]) if A[i] % A[0] != 0 else A[i]
            after_min = min(after_min, A[i])

        # print(A)
        if before_min == after_min:
            print(before_min)
            exit()

main()
