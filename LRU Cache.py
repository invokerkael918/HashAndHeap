class linkedNode():
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class LRUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # do intialization if necessary
        self.key_to_prev = {}
        self.dummy = linkedNode()
        self.tail = self.dummy
        self.capacity = capacity

    def push_back(self, node):
        # 因为要把node放到最后，所以此node的prev为当前的tail
        self.key_to_prev[node.key] = self.tail
        # 当前tail的下一位设置为 input node
        self.tail.next = node
        # 重新定义当前tail为 input node
        self.tail = node

    def pop_front(self):
        # dummy->6->7->9, head is 6
        head = self.dummy.next
        # key_to_prev {6:dummy,7:6,9:7,None:9}
        # {7:6,9:7,None:9} => {7:dummy,9:7,None:9}
        del self.key_to_prev[head.key]
        # dummy.next 指向 head.next(7)
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy

    def kick(self, prev):
        node = prev.next
        # dummy->6 ->7 prev = 6 , node =7=tail
        if node == self.tail:
            return
        # dummy->1->2->3->4 prev = 1 node = 2,node.next = 3
        # dummy-> 1->3->4 在链表种跳过node从prev连上node.next
        prev.next = node.next
        # dummy-> 1->3->4 node.next is 3, not None
        if node.next is not None:
            # 在哈希表里连上之前的
            self.key_to_prev[node.next.key] = prev
            node.next = None
        self.push_back(node)

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        # write your code here
        if key not in self.key_to_prev:
            return -1
        self.kick(self.key_to_prev[key])
        # key_to_prev[key].next得到node
        return self.key_to_prev[key].next.value

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        # write your code here
        if key in self.key_to_prev:
            # 被使用所以kick
            self.kick(self.key_to_prev[key])
            self.key_to_prev[key].next.value = value
        else:
            self.push_back(linkedNode(key, value))
            if len(self.key_to_prev) > self.capacity:
                self.pop_front()
