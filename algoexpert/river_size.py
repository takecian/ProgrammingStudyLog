def riverSizes(matrix):
    if not matrix or not matrix[0]:
        return []
    H = len(matrix)
    W = len(matrix[0])
    dones = set()
    ans = []
    for h in range(H):
        for w in range(W):
            if matrix[h][w] == 1 and (h, w) not in dones:
                dones.add((h, w))
                size = count_size(h, w, matrix)
                ans.append(size)

    return ans


def count_size(sh, sw, matrix):
    H = len(matrix)
    W = len(matrix[0])
    stack = [(sh, sw)]
    matrix[sh][sw] = 0
    size = 0
    while stack:
        h, w = stack.pop()
        size += 1
        for dh, dw in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            next_h = h + dh
            next_w = w + dw
            if 0 <= next_h < H and 0 <= next_w < W:
                if matrix[next_h][next_w] == 1:
                    matrix[next_h][next_w] = 0
                    stack.append((next_h, next_w))

    return size
