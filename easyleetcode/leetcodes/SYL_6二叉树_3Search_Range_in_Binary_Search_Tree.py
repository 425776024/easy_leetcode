

class Solution:
    res = []

    def searchRange(self, root, k1, k2):
        self.inorder_dfs(root, k1, k2)
        return self.res

    def inorder_dfs(self, root, k1, k2):
        if root is None:
            return None
        # 涉及到二叉查找树的按序输出，应马上联想到二叉树的中序遍历
        # 对于二叉查找树而言，使用中序遍历即可得到有序元素
        if root.left and root.val > k1:
            self.inorder_dfs(root.left, k1, k2)

        if k1 <= root.val <= k2:
            self.res.append(root.val)

        if root.right and root.val < k2:
            self.inorder_dfs(root.right, k1, k2)
