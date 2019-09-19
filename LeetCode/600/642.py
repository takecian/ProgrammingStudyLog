class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.sentences = sentences
        self.times = times
        self.text = ''

    def input(self, c: str) -> List[str]:
        if c == '#':
            try:
                self.times[self.sentences.index(self.text)] += 1
            except ValueError:
                self.sentences.append(self.text)
                self.times.append(1)
            self.text = ''
            return []

        self.text += c
        candidate = []
        for i in range(len(self.sentences)):
            if self.sentences[i].startswith(self.text):
                candidate.append((self.times[i], self.sentences[i]))
        candidate.sort(key=lambda x: (-x[0], x[1]))
        return list(map(lambda x: x[1], candidate[:3]))

