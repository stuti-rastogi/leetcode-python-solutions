# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def _level_order_traverse(self, root):
        """
            Returns a list of lists with levels of tree
        """
        level_order_traversal = []
        level = [root]
        while level:
            next_level = []
            for node in level:
                if node:
                    next_level.append(node.left)
                    next_level.append(node.right)
            level_order_traversal.append(level)
            if not any(next_level):
                break
            level = next_level
        return level_order_traversal


    def encode_string(self, level_order_traversal):
        encoded_string = ""
        for level in level_order_traversal:
            for node in level:
                if node:
                    encoded_string += str(node.val) + '/'
                else:
                    encoded_string += 'x/'
        return encoded_string[:-1]


    def construct_tree(self, traversal):
        traversal_len = len(traversal)

        root = TreeNode(int(traversal[0]))
        node_queue = [root]

        child = 1
        left_child = True
        fetch_new_node = True
        while child < traversal_len:
            if left_child:
                curr_node = node_queue.pop(0)
            if traversal[child] != 'x':
                new_node = TreeNode(int(traversal[child]))
            else:
                new_node = None
            if left_child:
                curr_node.left = new_node
                left_child = False
            else:
                curr_node.right = new_node
                left_child = True
            if new_node:
                node_queue.append(new_node)
            child += 1
        return root


    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        level_order_traversal = self._level_order_traverse(root)
        encoded_string = self.encode_string(level_order_traversal)
        return encoded_string


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        flat_traversal = data.split('/')
        return self.construct_tree(flat_traversal)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))