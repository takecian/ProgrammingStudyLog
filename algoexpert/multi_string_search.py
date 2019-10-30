from collections import defaultdict


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.is_word = False

    def add(self, word):
        node = self
        for char in word:
            node = node.children[char]
        node.is_word = True

    def find(self, word):
        node = self
        for char in word:
            if char not in node.children:
                return False
                node = node.children[char]

        return True

def multiStringSearch(bigString, smallStrings):
    # Write your code here.
    trie = Trie()
    words = bigString.split(' ')
    for word in words:
        trie.add(word)

    ans = []
    for word in smallStrings:
        ans.append(trie.find(word))
    return ans


print(multiStringSearch('Mary goes to the shopping center every week.', ['to', 'Mary', 'centers', 'shop', 'shopping']))
# print(multiStringSearch('this is a big string', ['kappa']))
# print(multiStringSearch('this is a big string', ['this', 'yo', 'is', 'a', 'bigger','string', 'kappa']))
