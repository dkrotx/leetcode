# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        prev = head
        cur = head.next
        head.next = None
        
        while cur:
            saved_next = cur.next
            cur.next = prev
            prev = cur
            cur = saved_next
            
        return prev
