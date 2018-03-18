# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        def list_len():
            n, node = 0, root
            while node:
                node = node.next
                n += 1
            return n
        
        n = list_len()
        part_size = n // k
        nbig_parts = n % k
        
        parts = []
        cur = root
        for _ in range(k):
            cur_size = part_size + int(len(parts) < nbig_parts)
            parts.append(cur)
            
            for x in range(cur_size - 1):
                cur = cur.next if cur else None
                
            if cur:
                next_head = cur.next
                cur.next = None # terminate current part
                cur = next_head
            
        return parts
