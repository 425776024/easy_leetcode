
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # 首先看当前结点是否为空，若为空则直接返回空，若为p或q中的任意一个，也直接返回当前结点

        if not root or p == root or q == root:
            return root
        # 因为是递归，left返回了值，又不和p,q相等，则是最小：公共父节点
        left = self.lowestCommonAncestor(root.left, p, q)
        if left and left != p and left != q:
            return left

        right = self.lowestCommonAncestor(root.right, p, q)

        # root is the LCA of p and q
        # 若p和q分别位于左右子树中，那么对左右子结点调用递归函数，会分别返回p和q结点的位置，
        # 而当前结点正好就是p和q的最小共同父结点，直接返回当前结点即可
        if left and right:
            return root
        # 都在右边
        # 可能叶子节点，返回的left,right是None，有才返回
        if left:
            return left
        if right:
            return right
