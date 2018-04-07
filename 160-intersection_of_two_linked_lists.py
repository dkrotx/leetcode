# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        def getTail(node):
            prev = None
            n = 0
            while node:
                prev = node
                node = node.next
                n += 1
            return (n, prev)
        
        def getNthNode(node, n):
            while n > 0:
                node = node.next
                n -= 1
                
            return node
        
        n_a, tail_a = getTail(headA)
        n_b, tail_b = getTail(headB)
        
        if not tail_a or tail_a is not tail_b:
            return None
        
        """ start from equal distance to the end """
        node_a = getNthNode(headA, n_a - n_b)
        node_b = getNthNode(headB, n_b - n_a)
        
        while node_a is not node_b:
            node_a = node_a.next
            node_b = node_b.next
            
        return node_a
