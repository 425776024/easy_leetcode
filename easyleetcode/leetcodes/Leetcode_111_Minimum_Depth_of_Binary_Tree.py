

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    '''
    首先判空，若当前结点不存在，直接返回0。然后看若左子结点不存在，那么对右子结点调用递归函数，并加1返回。
    反之，若右子结点不存在，那么对左子结点调用递归函数，并加1返回。
    若左右子结点都存在，则分别对左右子结点调用递归函数，将二者中的较小值加1返回即可
    '''

    def minDepth2(self, root):
        if root is None:
            return 0
        ld = self.minDepth(root.left)
        rd = self.minDepth(root.right)
        if root.left == None:
            return 1 + rd
        elif root.right == None:
            return 1 + ld

        return 1 + min(ld, rd)

    def minDepth(self, root):
        if root is None:
            return 0
        queue = [root]
        depth = 0
        while len(queue) > 0:
            depth += 1
            # 遍历每一层，遍历完这一层就pop完了
            q_len = len(queue)
            for i in range(q_len):
                node = queue.pop(0)
                if node.left is None and node.right is None:
                    return depth
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return -1
