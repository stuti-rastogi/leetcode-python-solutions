class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.positions = {}     # store corresponding positions of values in set
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.positions:
            # this is O(1) for dictionary
            self.values.append(val)
            self.positions[val] = len(self.values)-1       # last element added
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.positions:
            index = self.positions[val]
            lastElement = self.values[-1]
            self.values[index] = lastElement
            self.positions[lastElement] = index
            self.values.pop()
            self.positions.pop(val)
            return True
        return False
        
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.values[random.randint(0, len(self.values)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()