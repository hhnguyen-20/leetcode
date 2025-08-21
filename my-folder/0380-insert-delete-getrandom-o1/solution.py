class RandomizedSet:

    def __init__(self):
        self.values = []
        self.indexes = {} 

    def insert(self, val: int) -> bool:
        if val in self.indexes:
            return False
        
        self.indexes[val] = len(self.values)
        self.values.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.indexes:
            return False
        
        index = self.indexes[val]
        self.values[index] = self.values[-1]
        self.indexes[self.values[-1]] = index
        self.values.pop()
        del self.indexes[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
