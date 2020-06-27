class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        if root is None:
            return True
        if self.getDepth(root) == False:
            return False
        return True

    def getDepth(self, node):
        if node is None:
            return 1
        ld = self.getDepth(node.left)
        if ld < 0:
            return -1
        rd = self.getDepth(node.right)
        if rd < 0:
            return -1
        # 任一节点下，左右子数深度相差超过1，不是平衡树
        elif abs(ld - rd) > 1:
            return False
        else:
            return max(ld, rd) + 1


n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(17)

n1.left = n2
n1.right = n3

n3.left = n4
n3.right = n5

print(Solution().isBalanced(n1))
