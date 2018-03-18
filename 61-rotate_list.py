# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        def list_len():
            n = 0
            prev, node = None, head
            while node:
                prev, node = node, node.next 
                n += 1
            return n, prev
        
        def get_ith(i):
            node = head
            for _ in range(i):
                node = node.next
            return node
        
        n, tail = list_len()
        if n < 2:
            return head
        
        k %= n
        if k == 0:
            return head
        
        new_tail = get_ith(n - k - 1)
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        
        return new_head
