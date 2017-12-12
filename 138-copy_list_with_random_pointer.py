# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
            
        origin_nodes = []
        node = head
        prev_copy = None
        while node:
            origin_nodes.append(node)
            
            copy = RandomListNode(node.label)
            if prev_copy:
                prev_copy.next = copy
            prev_copy = copy
                
            next = node.next
            node.next = copy # we have to hold pointer to copy of this node to match random
            node = next
            
        new_head = origin_nodes[0].next
        
        # set pointers to random node in copy
        for old in origin_nodes:
            if old.random:
                old.next.random = old.random.next
        
        # restore "next" pointers in original list
        for i in range(len(origin_nodes)-1):
            origin_nodes[i].next = origin_nodes[i+1]
        origin_nodes[-1].next = None
        
        return new_head
