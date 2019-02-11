# https://abc076.contest.atcoder.jp/tasks/abc076_c

Sd = input()
T = input()

is_replaced = False
for i in range(len(Sd) - len(T), -1, -1):
    can_replace = True
    k = i
    j = 0
    while can_replace and j < len(T):
        if Sd[k] == T[j] or Sd[k] == "?":
            k += 1
            j += 1
        else:
            can_replace = False
            break

    if can_replace:
        # let's replace
        Sd_l = list(Sd)
        for ti in range(len(T)):
            Sd_l[i + ti] = T[ti]
        Sd = "".join(Sd_l)
        is_replaced = True
        break

if is_replaced:
    print(Sd.replace('?', 'a'))
else:
    print("UNRESTORABLE")
