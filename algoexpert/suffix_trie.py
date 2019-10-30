# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        n = len(string)

        for i in range(n):
            node = self.root
            for j in range(i, len(string)):
                key = string[j]
                if key not in node:
                    node[key] = {}
                node = node[key]
            node[self.endSymbol] = True

    def contains(self, string):
        node = self.root
        for char in string:
            if char not in node:
                return False
            node = node[char]
        return self.endSymbol in node


print(SuffixTrie('test'))
