# 递归
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        if root is None:
            return []
        else:
            return self.postorderTraversal(root.left) + \
                   self.postorderTraversal(root.right) + [root.val]


class Solution2:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        result = []
        if root is None:
            return result
        s = []
        # previously traversed node
        prev = None
        s.append(root)
        while s:
            curr = s[-1]
            # 是否无左右子节点
            noChild = curr.left is None and curr.right is None
            # 子节点是否被查看
            childVisited = (prev is not None) and (curr.left == prev or curr.right == prev)
            # 无子节点，或者子节点被查看（记录）了，就记录当前节点。否则，有右子节点就加入，有左子节点就加入（这样pop出来的先是做节点数据）
            if noChild or childVisited:
                result.append(curr.val)
                s.pop()
                prev = curr
            else:
                if curr.right is not None:
                    s.append(curr.right)
                if curr.left is not None:
                    s.append(curr.left)

        return result

# 反转先序遍历，『左右根』的后序遍历结果，我们发现只需将『根右左』的结果转置即可
# 先序遍历通常为『根左右』，故改变『左右』的顺序即可，所以如此一来后序遍历的非递归实现起来就非常简单了。

# class Solution3: 先序遍历，不会？？ 然后return res[::-1]，厉害了