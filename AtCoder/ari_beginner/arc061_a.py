# https://arc061.contest.atcoder.jp/tasks/arc061_a

S = list(input())
# print(S)

answer = 0
for i in range(1 << (len(S)-1)):
    expression = []
    for j in range(len(S)):
        if (i >> j) & 1:
            expression.append("{}+".format(S[j]))
        else:
            expression.append(S[j])
    # print(eval("".join(expression)))
    answer += eval("".join(expression))

print(answer)
