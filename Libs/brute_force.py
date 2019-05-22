def brute_force(s, candidates, remain):
    if remain == 0:
        print(s)
    else:
        for c in candidates:
            brute_force(s + c, candidates, remain - 1)


brute_force("", 'abc', 3)

# aaa
# aab
# aac
# aba
# abb
# abc
# aca
# acb
# acc
# baa
# bab
# bac
# bba
# bbb
# bbc
# bca
# bcb
# bcc
# caa
# cab
# cac
# cba
# cbb
# cbc
# cca
# ccb
# ccc