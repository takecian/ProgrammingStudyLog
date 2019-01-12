import copy

N, Q = map(int, input().split())
master_A = list(map(int, input().split()))

X = [int(input()) for _ in range(Q)]


for x in X:
    # start game
    A = copy.copy(master_A)

    takashi = 0

    aoki_pointer = 0
    for a in range(len(A)):
        if A[a] > x:
            break
        aoki_pointer = a

    while len(A) > 0:
        # takaeshi turn
        takashi += A[-1]
        del A[-1]

        # aoki turn
        if len(A) > 0:
            del_target = min(len(A) - 1, aoki_pointer)
            del A[del_target]

    print(takashi)
