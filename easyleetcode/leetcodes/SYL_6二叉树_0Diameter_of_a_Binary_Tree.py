class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.nodes = 1

        def depth(node):
            # 计算以node为终点的最大路径
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            # 节点是左右节点 + 1。（4节点直径是3）
            # L + R + 1 : L(2,4)  + R(3) + root(1)
            self.nodes = max(self.nodes, L + R + 1)
            # 最长路径节点（深度），你不能每个路径都要，只能要最大的
            return max(L, R) + 1

        depth(root)
        # number of nodes - 1 = length
        return self.nodes - 1


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)

n1.left = n2
n1.right = n3

n2.left = n4
n2.right = n5
s = Solution()
a = s.diameterOfBinaryTree(n1)
print(a)
