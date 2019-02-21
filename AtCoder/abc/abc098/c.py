N = int(input())
S = list(input())

e_count = S.count('E')
w_count = S.count('W')

# print(e_count)
# print(w_count)


left_w = 0
right_e = e_count
min_cost = len(S)-1

for i in range(len(S)):
    if i > 0:
        if S[i-1] == 'W':
            left_w += 1
    if S[i] == 'E':
        right_e -= 1
    cost = left_w + right_e
    if cost < min_cost:
        min_cost = cost

print(min_cost)
