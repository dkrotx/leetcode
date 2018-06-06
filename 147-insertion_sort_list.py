# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, cur = None, head
        while cur:
            following = cur.next
            
            # find place to insert
            prev_bigger, bigger = None, head
            while bigger and bigger is not cur and bigger.val < cur.val:
                prev_bigger = bigger
                bigger = bigger.next
                    
            if bigger and bigger is not cur:
                prev.next = cur.next
                cur.next = bigger
                
                if prev_bigger:
                    prev_bigger.next = cur
                else:
                    head = cur
            else:
                prev = cur
            
            cur = following
            
        return head
