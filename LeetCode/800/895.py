import collections
class FreqStack(object):

    def __init__(self):
        self.freq_counter = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        new_freq = self.freq_counter[x] + 1
        self.freq_counter[x] = new_freq
        self.maxfreq = max(self.maxfreq, new_freq)
        self.group[new_freq].append(x)

    def pop(self):
        x = self.group[self.maxfreq].pop()
        self.freq_counter[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()