class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        words = list(map(lambda w: w[::-1], words))
        return ' '.join(words)