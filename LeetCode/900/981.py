from collections import defaultdict
import bisect


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamps = defaultdict(list)
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        pos = bisect.bisect(self.timestamps[key], timestamp)
        if len(self.timestamps[key]) == pos:
            self.timestamps[key].append(timestamp)
            self.values[key].append(value)
        else:
            self.timestamps[key].insert(pos, timestamp)
            self.values[key].insert(pos, value)

    def get(self, key: str, timestamp: int) -> str:
        pos = bisect.bisect(self.timestamps[key], timestamp) - 1
        # print('{} {}'.format(pos, len(self.timestamps[key])))
        if pos == -1:
            return ''

        return self.values[key][pos]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)