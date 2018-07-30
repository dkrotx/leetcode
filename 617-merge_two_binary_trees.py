class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        return self.mergeSubTrees(t1, t2)
    
    def mergeSubTrees(self, n1, n2):
        def node_content(node):
            if node:
                return node.val, node.left, node.right
            return 0, None, None
        
        if not n1 and not n2:
            return None
        
        n1_val, n1_left, n1_right = node_content(n1)
        n2_val, n2_left, n2_right = node_content(n2)
        
        new_node = TreeNode(n1_val + n2_val)
        new_node.left = self.mergeSubTrees(n1_left, n2_left)
        new_node.right = self.mergeSubTrees(n1_right, n2_right)
        return new_node
