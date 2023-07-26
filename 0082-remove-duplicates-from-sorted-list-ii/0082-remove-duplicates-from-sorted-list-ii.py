# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        current = head

        while current:
        # Check if the current node has duplicates
            if current.next and current.val == current.next.val:
            # Skip all the duplicates
                while current.next and current.val == current.next.val:
                    current = current.next
            # Move to the next distinct node
                current = current.next
            # Update the prev node to skip the duplicates
                prev.next = current
            else:
            # Move both pointers to the next nodes
                prev = prev.next
                current = current.next

        return dummy.next