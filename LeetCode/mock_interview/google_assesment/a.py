from collections import Counter
import copy

class Solution:

    def solve(self, counter):
        ans = 0
        for key in counter.keys():
            if counter[key] > 0:
                new_counter = copy.deepcopy(counter)
                new_counter[key] -= 1
                ans = ans + 1 + self.solve(new_counter)

        return ans

    def numTilePossibilities(self, tiles: str) -> int:
        tile_l = list(tiles)
        counter = Counter(tile_l)
        ans = self.solve(counter)
        return ans

