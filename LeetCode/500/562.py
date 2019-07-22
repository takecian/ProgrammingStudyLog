class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        ans = 0
        if not M:
            return 0

        H = len(M)
        W = len(M[0])
        # horizontal
        for h in range(H):
            w = 0
            count = 0
            while w < W:
                if M[h][w] == 1:
                    count += 1
                    ans = max(ans, count)
                else:
                    count = 0
                w += 1

        # vertical
        for w in range(W):
            h = 0
            count = 0
            while h < H:
                if M[h][w] == 1:
                    count += 1
                    ans = max(ans, count)
                else:
                    count = 0
                h += 1
            print(ans)

        # diagonal
        for w in range(W):
            h = 0

            i = h
            j = w

            count = 0
            while i < H and j < W:
                if M[i][j] == 1:
                    count += 1
                    ans = max(ans, count)
                else:
                    count = 0
                i += 1
                j += 1

        for h in range(H):
            w = 0

            i = h
            j = w

            count = 0
            while i < H and j < W:
                if M[i][j] == 1:
                    count += 1
                    ans = max(ans, count)
                else:
                    count = 0
                i += 1
                j += 1

        # anti-diagonal
        for w in range(W):
            h = 0

            i = h
            j = w

            count = 0
            while i < H and 0 <= j:
                if M[i][j] == 1:
                    count += 1
                    ans = max(ans, count)
                else:
                    count = 0
                i += 1
                j -= 1

        for h in range(H):
            w = W - 1

            i = h
            j = w
            count = 0
            while i < H and 0 <= j:
                if M[i][j] == 1:
                    count += 1
                    ans = max(ans, count)
                else:
                    count = 0
                i += 1
                j -= 1

        return ans