# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return head
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1
        tail.next = head
        for _ in range(length - k % length):
            tail = tail.next
        new_head = tail.next
        tail.next = None
        return new_head