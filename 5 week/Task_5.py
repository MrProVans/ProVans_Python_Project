"""
380. Insert Delete GetRandom O(1)
Medium
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present.
Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present.
Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements
(it's guaranteed that at least one element exists when this method is called).
Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
"""

import random


class RandomizedSet:

    def __init__(self):
        self.val_to_index = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False

        index = self.val_to_index[val]
        last_element = self.values[-1]

        self.values[index] = last_element
        self.val_to_index[last_element] = index

        self.values.pop()
        del self.val_to_index[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


randomized_set = RandomizedSet()

print(randomized_set.insert(1))
print(randomized_set.insert(2))
print(randomized_set.insert(2))

print(randomized_set.getRandom())

print(randomized_set.remove(1))
print(randomized_set.remove(3))

print(randomized_set.getRandom())
