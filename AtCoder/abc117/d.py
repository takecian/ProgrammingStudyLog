# https://atcoder.jp/contests/abc117/tasks/abc117_d
from operator import add

N, K = map(int, input().split())
A = list(map(int, input().split()))

all_sum = [0 for _ in range(47)]
for a in A:
    l = list(map(int, list(format(a, '047b'))))
    # print(l)
    all_sum = list(map(add, all_sum, l))

# print("")
# print(all_sum)

mask = list(map(lambda x: 0 if x >= N / 2 else 1, all_sum))
# print(mask)

max_k = list(map(int, list(format(K, '047b'))))
# print(max_k)

idx = max_k.index(1)
next_k = []
for i in range(len(max_k)):
    if i < idx:
        next_k.append(max_k[i])
    elif i == idx:
        next_k.append(0)
    else:
        next_k.append(1)
# print(next_k)


def run_mask(msk, kk):
    k_list = []
    for e, ma in zip(mask, max_k):
        k_list.append(1 if e and ma else 0)

    # print(answer_k_list)
    answer_k = int("".join(map(str, k_list)), 2)
    # print(answer_k)
    return answer_k


k1 = run_mask(mask, max_k)
k2 = run_mask(mask, next_k)

answer_k = k1 if k1 > k2 else k2

result = 0
for a in A:
    result += a ^ answer_k

print(result)
