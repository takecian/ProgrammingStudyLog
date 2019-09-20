class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        # i 本置いた時の一番低い高さを dp に入れる
        for i in range(1, n + 1):
            max_width = shelf_width
            max_height = 0
            # i本目(j-1) から右寄せで新しい棚に置いた時に一段下の棚の高さがどこまで下がるか
            j = i - 1
            while j >= 0 and max_width - books[j][0] >= 0:
                max_width -= books[j][0]
                max_height = max(max_height, books[j][1])
                dp[i] = min(dp[i], dp[j] + max_height)
                print(dp)
                j -= 1
        return dp[n]