# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        last_odd = head
        first_even = last_even = head.next
        
        cur = first_even.next
        while cur:
            last_odd.next = cur
            last_odd = cur
            cur = cur.next
            
            if cur:
                last_even.next = cur
                last_even = cur
                cur = cur.next
        
        last_odd.next = first_even
        last_even.next = None
        return head
