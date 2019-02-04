# https://atcoder.jp/contests/abc079/tasks/abc079_c

ticket = list(input())

for i in range(1 << (len(ticket)-1)):
    exp = []
    for j in range(len(ticket)-1):
        if (i >> j) & 1:
            exp.append("{}+".format(ticket[j]))
        else:
            exp.append("{}-".format(ticket[j]))
    exp.append(ticket[-1])

    e = "".join(exp)
    if eval(e) == 7:
        print("{}={}".format(e, eval(e)))
        exit()
