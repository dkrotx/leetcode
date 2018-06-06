# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def list_len(head):
            n = 0
            while head:
                head = head.next
                n += 1
            return n
        
        def sum_by_ptrs(p1, p2):
            if p1 is None:
                return p2.val
            if p2 is None:
                return p1.val
            return p1.val + p2.val
        
        def advance_ptr(ptr, head, list_len, i):
            if ptr:
                return ptr.next
            return head if i == list_len else None
        
        def reverse_list(head):
            prev = None
            item = head
            while item:
                following = item.next
                item.next = prev
                prev = item
                item = following
                
            return prev # it's new head
        
        def normalize_list(head):
            last_node = head
            carry = 0
            
            while head:
                head.val += carry
                if head.val >= 10:
                    carry = head.val // 10
                    head.val = head.val % 10
                else:
                    carry = 0
                
                last_node = head
                head = head.next
                
            if carry:
                last_node.next = ListNode(carry)
                
        
        len1, len2 = list_len(l1), list_len(l2)
        ptr1, ptr2 = None, None
        res_head, res_prev = None, None
        
        for i in reversed(range(1, 1+max(len1, len2))):
            ptr1 = advance_ptr(ptr1, l1, len1, i)
            ptr2 = advance_ptr(ptr2, l2, len2, i)

            node = ListNode(sum_by_ptrs(ptr1, ptr2))
            if not res_head:
                res_head = node
            else:
                res_prev.next = node
            res_prev = node
            
            i -= 1
            
        res_head = reverse_list(res_head) # make significant digits last
        normalize_list(res_head)
        return reverse_list(res_head)     # return back, to significant digits first
