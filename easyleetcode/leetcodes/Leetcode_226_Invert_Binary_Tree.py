class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        # 层次遍历，交换左右点
        if root is None:
            return None
        queue = [root]
        while len(queue):
            curr = queue.pop(0)
            curr.left, curr.right = curr.right, curr.left
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
        return root

    def invertBinaryTree2(self, root):
        if root is None:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertBinaryTree2(root.left)
        self.invertBinaryTree2(root.right)
        return root
