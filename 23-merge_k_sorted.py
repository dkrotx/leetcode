import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res_head, res_tail = None, None
        
        def value_item_pair(item, uid):
            return (item.val, uid, item)
        
        uid = 0 # for stable sorting in heapq
        h = []
        for item in filter(lambda lst: lst, lists):
            heapq.heappush(h, value_item_pair(item, uid))
            uid += 1
            
        while h:
            val, uid, item = heapq.heappop(h)
            
            node = ListNode(val)
            if res_head is None:
                res_head = node
            if res_tail:
                res_tail.next = node
            res_tail = node
            
            if item.next:
                heapq.heappush(h, value_item_pair(item.next, uid))
                
        return res_head
