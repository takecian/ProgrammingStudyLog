# https://atcoder.jp/contests/abc049/tasks/arc065_a

S = input()

#
# def is_composable(s):
#     if len(s) == 0:
#         return True
#
#     if s.startswith("dreamer"):
#         dream_s = s[5:]
#         dreamer_s = s[7:]
#         return is_composable(dream_s) or is_composable(dreamer_s)
#     elif s.startswith("dream"):
#         dream_s = s[5:]
#         return is_composable(dream_s)
#     elif s.startswith("eraser"):
#         erase_s = s[5:]
#         eraser_s = s[6:]
#         return is_composable(erase_s) or is_composable(eraser_s)
#     elif s.startswith("erase"):
#         erase_s = s[5:]
#         return is_composable(erase_s)
#     else:
#         return False
#
#
# if len(S) > 0 and is_composable(S):
#     print("YES")
# else:
#     print("NO")

S = S[::-1]

dream = "maerd"
dreamer = "remaerd"
erase = "esare"
eraser = "resare"

if len(S) > 0:
    while len(S) > 0:
        if S.startswith(dream):
            S = S[len(dream):]
        elif S.startswith(dreamer):
            S = S[len(dreamer):]
        elif S.startswith(erase):
            S = S[len(erase):]
        elif S.startswith(eraser):
            S = S[len(eraser):]
        else:
            break
    if len(S) > 0:
        print("NO")
    else:
        print("YES")

else:
    print("NO")
