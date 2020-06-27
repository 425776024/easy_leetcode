
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def buildTree(self, inorder, postorder):
        if not postorder:
            return None
        root = TreeNode(postorder[-1])  # 创建树
        n = inorder.index(root.val)
        # inorder：左根右
        # postorder：左右根
        # 拿到根index ：n，:n都是左边值
        root.left = self.buildTree(inorder[:n], postorder[:n])
        # postorder：n:-1是右边值
        root.right = self.buildTree(inorder[n + 1:], postorder[n:-1])
        return root
