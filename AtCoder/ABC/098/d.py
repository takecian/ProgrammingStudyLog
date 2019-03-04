# note solved
N = int(input())
A = list(map(int, input().split()))

match = 0
for l in range(len(A)):
    base = A[l]
    match += 1
    for r in range(l+1, len(A)):
        ando = base & A[r]
        if ando == 0:
            match += 1
        else:
            break
        base |= A[r]

print(match)
