# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        firstChild = root
        while firstChild:
            prev = None
            node, firstChild = firstChild, None
            
            while node:
                for child in filter(None, [node.left, node.right]):
                    if not firstChild:
                        firstChild = child
                    if prev:
                        prev.next = child
                    prev = child

                node = node.next
