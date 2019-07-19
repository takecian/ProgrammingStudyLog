class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.big_int = 10 ** 10
        self.maps = [self.big_int] * (1000000 + 1)

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        self.maps[key] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        return self.maps[key] if self.maps[key] != self.big_int else -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        self.maps[key] = self.big_int
