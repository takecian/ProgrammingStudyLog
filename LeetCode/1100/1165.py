from collections import defaultdict


class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        # create distance map
        distance = defaultdict(lambda: defaultdict(int))

        n = len(keyboard)
        for i in range(n - 1):
            for j in range(i + 1, n):
                distance[keyboard[i]][keyboard[j]] = j - i
                distance[keyboard[j]][keyboard[i]] = j - i

        ans = distance[keyboard[0]][word[0]]

        for i in range(1, len(word)):
            ans += distance[word[i - 1]][word[i]]

        return ans
