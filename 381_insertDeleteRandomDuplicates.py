import random

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.elements = []
        self.indices = {}


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        notExists = False
        if val not in self.indices:
            self.indices[val] = set()
            notExists = True
        self.indices[val].add(len(self.elements))
        self.elements.append(val)
        return notExists


    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.indices:
            return False
        valIndex = self.indices[val].pop()
        if not self.indices[val]:
            self.indices.pop(val)
        
        if valIndex != len(self.elements)-1:
            lastValue = self.elements[-1]
            self.indices[lastValue].remove(len(self.elements)-1)
            self.indices[lastValue].add(valIndex)
            self.elements[valIndex] = lastValue
        
        self.elements.pop()
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.elements)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()