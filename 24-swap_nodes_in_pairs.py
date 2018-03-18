# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next):
            return head
        
        prev, cur = None, head
        head = cur.next
        
        while cur and cur.next:
            next_cur = cur.next.next
            cur.next.next = cur
            if prev:
                prev.next = cur.next
            prev, cur = cur, next_cur
            
        prev.next = cur
        return head
