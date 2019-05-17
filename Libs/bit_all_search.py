
# Bit 全探索
def bit_all_search(l):
    pattern = 1 << len(l)  # 1 をリストの長さだけ左にシフトする
    for i in range(pattern):
        scope = []
        for j in range(len(l)):
            if (i >> j) & 1:
                scope.append(l[j])
        # do something
        pass
