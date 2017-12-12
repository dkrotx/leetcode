# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListMaker:
    def __init__(self):
        self.head, self.tail = None, None
        
    def append(self, value):
        node = ListNode(value)
        
        if not self.head:
            self.head = node
        if self.tail:
            self.tail.next = node
            
        self.tail = node

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_list = ListMaker()
        cur, prev = head, None
        nrepeat = 0
        
        while cur:
            if prev and cur.val != prev.val:
                if nrepeat == 1:
                    new_list.append(prev.val)
                nrepeat = 0
                
            prev = cur
            cur = cur.next
            nrepeat += 1
            
        if nrepeat == 1:
            new_list.append(prev.val)
        
        return new_list.head
