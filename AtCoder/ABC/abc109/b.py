# https://atcoder.jp/contests/abc109/tasks/abc109_b

N = int(input())

words = {}
last_w = ""

for _ in range(N):
    w = input()
    if w in words:
        print("No")
        exit()
    else:
        if len(last_w) == 0 or last_w == w[0]:
            words[w] = True
            last_w = w[-1]
        else:
            print("No")
            exit()

print("Yes")

