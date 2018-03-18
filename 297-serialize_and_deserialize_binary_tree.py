# Definition for a binary tree node.
# class TreeNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None


class Codec:
    class TreeFormatError(Exception):
        pass
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        res = []
        layer = [root]

        while any(layer):
            next_layer = []
            for node in layer:
                if node:
                    next_layer.extend([node.left, node.right])
                    res.append(str(node.val))
                else:
                    res.append('#')
            layer = next_layer

        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        values = list(map(lambda x: None if x == '#' else int(x), data.split(',')))
        
        root = TreeNode(values[0])
        i, layer = 1, [root]
        while layer:
            next_layer = []
            for node in layer:
                if i < len(values):
                    if values[i] is not None:
                        node.left = TreeNode(values[i])
                        next_layer.append(node.left)
                    i += 1
                
                if i < len(values):
                    if values[i] is not None:
                        node.right = TreeNode(values[i])
                        next_layer.append(node.right)
                    i += 1

            layer = next_layer

        if i < len(values):
            raise Codec.TreeFormatError("Some values are not deserialized!")

        return root
