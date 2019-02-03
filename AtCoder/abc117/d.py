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

k = list(map(int, list(format(K, '047b'))))
# print(k)

answer_k_list = []
for e, ma in zip(mask, k):
    answer_k_list.append(1 if e and ma else 0)

# print(answer_k_list)
answer_k = int("".join(map(str, answer_k_list)), 2)
print(answer_k)

result = 0
for a in A:
    result += a ^ answer_k

print(result)
