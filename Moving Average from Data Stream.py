from collections import deque

class MovingAverage:
    """
    @param: size: An integer
    """

    def __init__(self, size):
        # do intialization if necessary
        self.queue = deque([])
        self.size = size
        self.sum = 0.0


    """
    @param: val: An integer
    @return:  
    """

    def next(self, val):
        # write your code here
        if len(self.queue) ==self.size:
            self.sum -= self.queue.popleft()

        self.sum+=val
        self.queue.append(val)
        return self.sum/ len(self.queue)
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)

if __name__ == '__main__':
    MovingAverage(3)
    next(1)
    next(10)
    next(3)
    next(5)
