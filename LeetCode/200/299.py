class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        rest = set()
        bulls = 0
        cow_secret = [0] * 10
        guess_secret = [0] * 10
        for i, j in zip(secret, guess):
            if i == j:
                bulls += 1
            else:
                cow_secret[int(i)] += 1
                guess_secret[int(j)] += 1

        cows = 0
        for i in range(10):
            cows += min(cow_secret[i], guess_secret[i])

        return '{}A{}B'.format(bulls, cows)