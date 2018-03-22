# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ptr1, ptr2 = head, None
        while ptr1:
            ptr1 = ptr1.next
            if n == 0:
                ptr2 = ptr2.next if ptr2 else head
            else:
                n -= 1
                
        # ptr2 will point to node BEFORE Nth
        if not ptr2:
            return head.next
        
        ptr2.next = ptr2.next.next
        return head
