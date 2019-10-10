class RandomizedSet:

    def __init__(self):
        # do intialization if necessary
        self.nums = []
        self.num_to_pos = {}

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """

    def insert(self, val):
        # write your code here
        if val in self.nums:
            return False
        self.nums.append(val)
        self.num_to_pos[val] = len(self.nums) - 1
        print(self.nums)
        print(self.num_to_pos)
        return True


    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """

    def remove(self, val):
        # write your code here
        if val not in self.nums:
            return False
        index,last = self.num_to_pos[val],len(self.nums)-1
        #{6:0,3:1,4:2}
        #remove(3)
        #{6:0,4:1}
        self.num_to_pos[self.nums[last]] = index
        self.nums[index],self.nums[last] = self.nums[last], self.nums[index]
        self.nums.pop()
        del self.num_to_pos[val]
        return True


    """
    @return: Get a random element from the set
    """

    def getRandom(self):
        # write your code here
        import random
        return random.choice(self.nums)

if __name__ == '__main__':
    #Your RandomizedSet object will be instantiated and called as such:
    obj = RandomizedSet()
    param = obj.insert(6)
    param = obj.insert(3)
    param = obj.insert(4)
    param = obj.remove(3)

