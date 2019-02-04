# https://beta.atcoder.jp/contests/abc006/tasks/abc006_3
# a + b + c = N
# 2a + 3b + 4c = M


N, M = map(int, input().split())
#
# ans_a = -1
# ans_a = -1
# ans_a = -1
#
# for a in range(N+1):
#     rest = N - a
#     for b in range(rest+1):
#         c = rest - b
#         if c < 0:
#             break
#         if 2 * a + 3 * b + 4 * c == M:
#             print(str(a) + ' ' + str(b) + ' ' + str(c) + '\n')
#             exit(0)
#
# print('-1 -1 -1\n')
#

# in case of 0 elder person
# a + c = N
# 2a + 4c = M
if M % 2 == 0:
    a = 2 * N - M // 2
    c = M // 2 - N
    if a >= 0 and c >= 0:
        print(str(a) + ' 0 ' + str(c) + '\n')
        exit(0)

if M % 2 == 1:
    a = 2 * N - (M + 1) // 2
    c = -N + (M - 1) // 2
    if a >= 0 and c >= 0:
        print(str(a) + ' 1 ' + str(c) + '\n')
        exit(0)

print('-1 -1 -1\n')

# in case of 1 elder person
# a + c = N - 1
# 2a + 4c = M - 3
