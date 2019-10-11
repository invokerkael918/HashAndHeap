class MyQueue:

    def __init__(self):
        # do intialization if necessary
        self.s1 = []
        self.s2 = []

    """
    @param: element: An integer
    @return: nothing
    """

    def rebuild(self):
        if len(self.s2) == 0:
            while len(self.s1) != 0:
                self.s2.append(self.s1.pop())

    def push(self, element):
        # write your code here
        self.s1.append(element)

    """
    @return: An integer
    """

    def pop(self):
        # write your code here
        self.rebuild()
        return self.s2.pop()

    """
    @return: An integer
    """

    def top(self):
        # write your code here
        self.rebuild()
        return self.s2[(len(self.s2) - 1)]
