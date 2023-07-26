# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dh=ListNode(-1)
        dh.next=head
        cn=dh
        while cn and cn.next:
            if cn.next.val==val:
                cn.next=cn.next.next
            else :
                cn=cn.next
        return dh.next