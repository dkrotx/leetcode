class Solution:
    def reverseBetween(self, head, start, end):
        """
        :type head: ListNode
        :type start: int
        :type end: int
        :rtype: ListNode
        """
        
        if end == start:
            return head
        
        """ look for node before head of sublist to reverse """
        cur = None
        for _ in range(start - 1):
            cur = cur.next if cur else head
            
        beforehead = cur # may by null if reversing from start
        
        """ reverse sublist """
        new_tail = beforehead.next if beforehead else head
        prev = new_tail
        cur = prev.next
        
        for _ in range(end - start):
            saved_next = cur.next
            cur.next = prev
            prev, cur = cur, saved_next
        
        new_tail.next = cur    
        new_head = prev
        
        """ fix pointer of previous node """
        if beforehead:
            beforehead.next = new_head
        
        return new_head if start == 1 else head
