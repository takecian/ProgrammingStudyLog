def searchInSortedMatrix(matrix, target):
    # Write your code here.
    H = len(matrix)
    W = len(matrix[0])
    for h in range(H):
        for w in range(W):
            if matrix[h][w] == target:
                return [h, w]

            if matrix[h][w] > target:
                break

    return [-1, -1]