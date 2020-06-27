
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root):
        self.ans = float('-inf')
        self.getNodeMaxValue(root)
        return self.ans

    def getNodeMaxValue(self, node):
        # 得到以node结点为终点的 最大path 之和
        if not node: return 0
        # 得到以node.left结点为终点的 最大path 之和
        lresult = self.getNodeMaxValue(node.left)
        # 得到以node.right结点为终点的 最大path 之和
        rresult = self.getNodeMaxValue(node.right)
        # 左右最大路径和都知道了，如果小于0就不要了::max(l/r,0) ，如果大于0，那就拼上左右的和、和当前节点看能不能增加和
        # ans能拼接左右，但是函数返回值不能，不是同一个意思
        self.ans = max(self.ans, max(lresult, 0) + max(rresult, 0) + node.val)
        path_sum = max(lresult, rresult, 0)
        # 返回值是取 left 和 right 中的较大值加上当前结点值
        # 返回值的定义是以当前结点为终点的 最大path 之和，所以只能取 left 和 right 中较大的那个值，
        return max(0, path_sum + node.val)


n1 = TreeNode(-10)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)

n1.left = n2
n1.right = n3

n3.left = n4
n3.right = n5

print(Solution().maxPathSum(n1))
