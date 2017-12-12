# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def list_size(head):
    n = 0
    while head is not None:
        head = head.next
        n += 1
    return n
    
def nth_element(head, n):
    for i in range(n):
        head = head.next
    return head

class Solution(object):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    def sortList(self, head):
        def mergesort_list(head):
            """
            1. lookup middle of the list
               separate left part
            2. call mergesort_list for left and right subparts
            3. merge results
            """
            n = list_size(head)
            if n == 1:
                return head
            
            before_middle = nth_element(head, n/2 - 1)
            middle = before_middle.next
            before_middle.next = None
            
            left = mergesort_list(head)
            right = mergesort_list(middle)
            
            if left.val < right.val:
                new_head = left
                left = left.next
            else:
                new_head = right
                right = right.next

            tail = new_head 
                
            while left and right:
                if left.val < right.val:
                    tail.next = left
                    tail = left
                    left = left.next
                else:
                    tail.next = right
                    tail = right
                    right = right.next
            
            if left:
                tail.next = left
            elif right:
                tail.next = right
                
            return new_head

        if not head:
            return None
            
        return mergesort_list(head)
