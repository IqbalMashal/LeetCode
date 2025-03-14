class RandomizedSet:

    def __init__(self):
        self.set = {}
        self.size = 0
        

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False

        self.set[val] = val 
        return True

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False
        self.set.pop(val)
        return True  

    def getRandom(self) -> int:
        res = random.choice(list(self.set.values()))
        return res
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()