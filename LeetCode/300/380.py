class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_index = {}
        self.values = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.val_index:
            return False
        self.values.append(val)
        self.val_index[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.val_index:
            return False

        # replace last value info with removed value info
        remove_index = self.val_index[val]
        last_value = self.values[-1]

        self.val_index[last_value] = remove_index
        self.values[remove_index] = last_value

        # remove value info
        del self.val_index[val]
        self.values.pop()

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.values)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()