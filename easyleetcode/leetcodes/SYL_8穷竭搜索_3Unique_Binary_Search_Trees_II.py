

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    # @paramn n: An integer
    # @return: A list of root
    def generateTrees(self, n):
        return self.helper(1, n)

    def helper(self, start, end):
        # 递归地构造左右子树并将其链接到相应的根节点中
        result = []
        if start > end:
            result.append(None)
            return result
        for i in range(start, end + 1):
            # 小于i的数作为左子树，大于i的数作为右子树
            leftTree = self.helper(start, i - 1)
            rightTree = self.helper(i + 1, end)
            # 使用两重循环将左右子树所有可能的组合链接到以i为根节点的节点上。
            for j in range(len(leftTree)):
                for k in range(len(rightTree)):
                    root = TreeNode(i)
                    root.left = leftTree[j]
                    root.right = rightTree[k]
                    result.append(root)

        return result


s = Solution()
res = s.generateTrees(3)
print(res)
