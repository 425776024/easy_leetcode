
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        # 中序遍历得到一个排好序的二叉树，也可以非递归，参考，二叉树遍历
        a = lambda root: [] if not root else a(root.left) + [root.val] + a(root.right)
        self.lst = deque(a(root))

    def next(self) -> int:
        return self.lst.popleft()

    def hasNext(self) -> bool:
        return bool(self.lst)
