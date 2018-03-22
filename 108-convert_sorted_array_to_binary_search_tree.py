# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.constructTree(nums)
    
    def constructTree(self, arr):
        if not arr:
            return None
        
        mid = len(arr) // 2
        root = TreeNode(arr[mid])
        root.left = self.constructTree(arr[:mid])
        root.right = self.constructTree(arr[mid+1:])
        return root
