
class Solution:
    def isValidBST(self, root):
        if root == None: return True
        return self.valid(root, -(2 ** 32), 2 ** 32)

    def valid(self, root, low, high):
        if root == None: return True
        if root.val <= low or root.val >= high: return False
        # 左边 在 low : root.val之间
        # 右边 在 root.val : high之间
        # 则是二叉搜索树(左<根<右)
        return self.valid(root.left, low, root.val) and self.valid(root.right, root.val, high)
