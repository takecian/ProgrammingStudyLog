# https://atcoder.jp/contests/keyence2019/tasks/keyence2019_b

import re

S = input()

if "keyence" == S:
    print("YES")
else:
    patterns = ["^keyence(.*)", "^k(.*)eyence$", "^ke(.*)yence$", "^key(.*)ence$", "^keye(.*)nce$", "^keyen(.*)ce$", "^keyenc(.*)e$", "keyence$"]

    matched = False
    for pattern in patterns:
        matchOB = re.search(pattern, S)
        if matchOB:
            matched = True
            break
    if matched:
        print("YES")
    else:
        print("NO")


