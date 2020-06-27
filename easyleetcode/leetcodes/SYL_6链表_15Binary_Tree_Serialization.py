

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:

    def serialize(self, root):
        if not root:
            return ''

        def post_order(root):
            if root:
                # 先左->右->中
                post_order(root.left)
                post_order(root.right)
                ret[0] += str(root.val) + ','
            else:
                ret[0] += '#,'

        ret = ['']
        post_order(root)

        return ret[0][:-1]  # remove last ,

    def deserialize(self, data):
        if not data:
            return

        nodes = data.split(',')

        def post_order(nodes):
            if nodes[-1] == '#':
                nodes.pop()
                return None
            # 从最后一个值开始pop， 构成tree的时候， 就应该先中->右->左。
            v = nodes.pop()
            root = TreeNode(int(v))
            root.right = post_order(nodes)
            root.left = post_order(nodes)
            return root

        return post_order(nodes)


import collections


class Solution2:
    # serialize：根左右 顺序 变成 str
    # deserialize：根左右 顺序 变成 解析成二叉树
    def serialize(self, root):
        if not root:
            return

        ret = []
        queue = collections.deque()
        queue.append(root)
        # 前序遍历
        while queue:
            node = queue.popleft()
            if node:
                ret.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                ret.append('#')
        # 根左右
        return ','.join(ret)

    def deserialize(self, data):
        if not data:
            return
        nodes = data.split(',')
        # 根
        root = TreeNode(int(nodes[0]))
        i = 1
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            # 左
            if nodes[i] == '#':
                node.left = None
            else:
                t = TreeNode(int(nodes[i]))
                node.left = t
                queue.append(t)
            i += 1
            # 右
            if nodes[i] == '#':
                node.right = None
            else:
                t = TreeNode(int(nodes[i]))
                node.right = t
                queue.append(t)
            i += 1
        return root
