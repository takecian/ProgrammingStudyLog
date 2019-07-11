# https://leetcode.com/problems/letter-tile-possibilities/

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()
        ans.add('')
        for c in tiles:
            word = set()
            for a in ans:
                for i in range(len(a) + 1):
                    word.add(a[:i] + c + a[i:])
            # print(word)
            for w in word:
                ans.add(w)
        return len(ans) - 1
