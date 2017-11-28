# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import re

class Solution:
    re_tokens = re.compile(r'-?\d+|[\(\)]')
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """        
        self.tokens = re.findall(Solution.re_tokens, s)
        if self.tokens:
            return self.tree_from_tokens(0)
        
        return None
    
    def tree_from_tokens(self, i):
        node = TreeNode(int(self.tokens[i]))
        
        i += 1
        
        if i == len(self.tokens):
            return node
        
        if self.tokens[i] == ')':
            return i+1, node
        if self.tokens[i] == '(':
            i, node.left = self.tree_from_tokens(i+1)
            
        if i == len(self.tokens):
            return node
        
        if self.tokens[i] == ')':
            return i+1, node
        if self.tokens[i] == '(':
            i, node.right = self.tree_from_tokens(i+1)
        
        if i == len(self.tokens):
            return node
        
        assert(self.tokens[i] == ')')
        return i+1, node
