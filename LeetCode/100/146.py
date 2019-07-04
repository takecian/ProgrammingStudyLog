# https://leetcode.com/problems/lru-cache/

from collections import defaultdict


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.lru = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.lru:
            return -1

        self.lru.remove(key)
        self.lru.append(key)
        # print(self.lru)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.lru.remove(key)
            self.lru.append(key)
            self.cache[key] = value
        else:
            self.cache[key] = value
            self.lru.append(key)

            if len(self.lru) > self.capacity:
                self.cache.pop(self.lru[0])
                self.lru.pop(0)
        # print(self.lru)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)