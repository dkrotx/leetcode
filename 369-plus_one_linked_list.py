# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    @staticmethod
    def invert_list(node):
        prev = None
        
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
            
        return prev
        
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
            
        head = Solution.invert_list(head)
        node = head
        
        carry = 1
        while node:
            if node.val == 9:
                node.val = 0
                node = node.next
            else:
                node.val += 1
                carry = 0
                break
        
        head = Solution.invert_list(head)
        if carry: # add most significant '1'
            node = ListNode(1)
            node.next = head
            head = node
            
        return head
