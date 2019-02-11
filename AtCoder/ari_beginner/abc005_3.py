T = int(input())
N = int(input())
A = list(map(int, input().split()))  # tako
M = int(input())
B = list(map(int, input().split()))  # customer

A.sort()
B.sort()

can_sell = True
i = 0
j = 0
while j < len(B):
    while i < len(A) and (B[j] < A[i] or A[i] + T < B[j]):
        i += 1

    if i == len(A):
        can_sell = False
        break

    # print("Sell tako {}, for {}".format(A[i], B[j]))
    i += 1
    j += 1

if can_sell:
    print("yes")
else:
    print("no")


