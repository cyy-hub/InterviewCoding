# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs_ser(node, string):
            if node == None:
                string += "None,"
            else:
                string += "{0},".format(node.val)
                string = dfs_ser(node.left, string)
                string = dfs_ser(node.right, string)
            return string
        return dfs_ser(root, "")

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def dfs_deser(lis):
            if lis[0] == "None":
                lis.pop(0)
                return None
            root = TreeNode(lis[0])   # 不需要val么
            lis.pop(0)
            root.left = dfs_deser(lis)
            root.right = dfs_deser(lis)
            return root
        lis = data.split(",")
        return dfs_deser(lis)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))