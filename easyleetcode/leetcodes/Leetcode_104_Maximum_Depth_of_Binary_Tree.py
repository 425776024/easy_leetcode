

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        # 递归，没啥好说的
        if root is None:
            return 0
        ld = self.maxDepth(root.left)
        rd = self.maxDepth(root.right)
        return 1 + max(ld, rd)

    def maxDepth2(self, root):
        # 非递归，厉害了
        if None == root: return 0
        # 根节点开始，进行，层次遍历！
        q = []
        q.append(root)
        # 遍历一层，+1
        max_depth = 0
        while q != []:
            for i in range(len(q)):
                # 取出这层的全部节点！
                node = q[0]
                q.remove(node)

                if (node.left):
                    q.append(node.left)

                if (node.right):
                    q.append(node.right)
			# 过一层，+1
            max_depth += 1

        return max_depth
