class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split(' ')
        goat_words = []

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in range(len(words)):
            word = words[i]
            if word[0] not in vowels:
                word = word[1:] + word[0]

            goat_words.append(word + 'ma' + 'a' * (i + 1))
        return ' '.join(goat_words)
