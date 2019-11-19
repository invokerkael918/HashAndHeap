"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if not lists:
            return None

        return self.merge_range_lists(lists, 0, len(lists) - 1)

    def merge_range_lists(self, lists, start, end):
        if start == end:
            return lists[start]

        mid = (start + end) // 2
        left = self.merge_range_lists(lists, start, mid)
        right = self.merge_range_lists(lists, mid + 1, end)
        return self.mergeSortedArray(left, right)

    def mergeSortedArray(self, headA, headB):
        # write your code here
        tail = dummy = ListNode(0)
        while headA and headB:

            if headA.val > headB.val:
                tail.next = headB
                tail = headB
                headB = headB.next
            else:
                tail.next = headA
                tail = headA
                headA = headA.next

        if headA:
            while headA:
                tail.next = headA
                tail = headA
                headA = headA.next
        if headB:
            while headB:
                tail.next = headB
                tail = headB
                headB = headB.next

        return dummy.next