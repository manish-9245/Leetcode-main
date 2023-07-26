# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or k == 0:
            return head

    # Find the length of the linked list and locate the last node
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1

    # Create a cycle and adjust k to get the effective rotation count
        tail.next = head
        k %= length

    # Find the new tail node after rotation
        for i in range(length - k - 1):
            head = head.next

        new_head = head.next
        head.next = None

        return new_head