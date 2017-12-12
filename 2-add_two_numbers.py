# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    @staticmethod
    def add_item(value, prev):
        node = ListNode(value)
        prev.next = node
        return node
       
    @staticmethod
    # 807 -> (7 -> 0 -> 8)
    def pack_num(num):
        head = ListNode(num % 10)
        num = (num - num % 10) / 10
        cur = head
        
        while num > 0:
            digit = num % 10
            cur = Solution.add_item(digit, cur)
            num = (num - num % 10) / 10
            
        return head
    
    @staticmethod
    # convert (2 -> 4 -> 3) to int(342)
    def extract_num(lst):
        num = 0
        mul = 1
        cur = lst
        while cur:
            num += cur.val * mul
            mul *= 10
            cur = cur.next
            
        return num
        
    def addTwoNumbers(self, l1, l2):
        a = Solution.extract_num(l1)
        b = Solution.extract_num(l2)
        return Solution.pack_num(a+b)
