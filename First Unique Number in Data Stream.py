class ListNode():
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class DataStream:

    def __init__(self):
        # do intialization if necessary
        self.dummy = ListNode(0)
        self.tail = self.dummy
        self.num_to_prev = {}
        self.duplicates = set()

    """
    @param num: next number in stream
    @return: nothing
    """

    def add(self, num):
        # write your code here
        if num in self.duplicates:
            return
        if num not in self.num_to_prev:
            self.push_back(num)
            return
        # found duplicate one
        self.duplicates.add(num)
        self.remove(num)

    def remove(self, num):
        prev = self.num_to_prev[num]
        del self.num_to_prev[num]
        prev.next = prev.next.next
        if prev.next:
            self.num_to_prev[prev.next.val] = prev
        else:
            self.tail.prev

    """
    @return: the first unique number in stream
    """

    def firstUnique(self):
        # write your code here
        if not self.dummy.next:
            return None
        return self.dummy.next.val

    def push_back(self, num):
        self.tail.next = ListNode(num)
        self.num_to_prev[num] = self.tail
        self.tail = self.tail.next