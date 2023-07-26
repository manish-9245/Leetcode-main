# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a=""
        b=""
        while l1 is not None:
            a+=str(l1.val)
            l1=l1.next
        while l2 is not None:
            b+=str(l2.val)
            l2=l2.next
        a=a[::-1]
        b=b[::-1]
        ans=str(int(a)+int(b))
        anstr=ans[::-1]
        ans = trav = ListNode()
        for i in range(len(anstr)):
            trav.val = anstr[i]
            #prevent extra node at end
            if i != len(anstr) - 1 :
                trav.next = ListNode()
            trav = trav.next
        return ans