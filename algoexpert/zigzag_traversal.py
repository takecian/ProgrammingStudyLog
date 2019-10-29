def zigzagTraverse(array):
    # Write your code here.
    H = len(array)
    W = len(array[0])

    ans = []
    godown = True
    i = 0
    j = 0

    while is_inside(i, j, H, W):
        ans.append(array[i][j])
        if godown:
            if i == H - 1 or j == 0:
                godown = False
                if i == H - 1:
                    j += 1
                else:
                    i += 1
            else:
                i += 1
                j -= 1
        else:
            if i == 0 or j == W - 1:
                godown = True
                if j == W - 1:
                    i += 1
                else:
                    j += 1
            else:
                i -= 1
                j += 1

    return ans


def is_inside(h, w, H, W):
    return 0 <= h < H and 0 <= w < W