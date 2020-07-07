
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def buildTree(self, preorder, inorder):
        n = len(inorder)
        inOrderMap = {inorder[i]: i for i in range(n)}
        return self.buildTreeUtil(preorder, inorder, inOrderMap, 0, n - 1, 0, n - 1)

    def buildTreeUtil(self, preorder, inorder, inOrderMap, pStart, pEnd, iStart, iEnd):
        if pStart > pEnd or iStart > iEnd:
            return None
        # 根节点，永远是先序遍历第一个点
        root = TreeNode(preorder[pStart])
        # 根节点索引，根据它，找到中序遍历中根节点位置
        rootIdx = inOrderMap[root.val]
        # 根节点左边 //  rootIdx - iStart 得到左边节点数
        # 先序遍历(pStart + 1, pStart + rootIdx - iStart)(左边新起点，左边新终点（左边新起点+左边节点数）)
        root.left = self.buildTreeUtil(preorder, inorder, inOrderMap, pStart + 1, pStart + rootIdx - iStart, iStart,
                                       rootIdx - 1)
        # 根节点右边
        # 先序遍历(pStart + rootIdx - iStart+1)(左边新终点（左边新起点+左边节点数）的后一个数 （右边起点）)
        root.right = self.buildTreeUtil(preorder, inorder, inOrderMap, pStart + rootIdx - iStart + 1, pEnd, rootIdx + 1,
                                        iEnd)
        return root

    def buildTree2(self, preorder, inorder):
        if not preorder:
            return None
        # preorder：根左右
        # inorder：左根右
        x = preorder.pop(0)
        node = TreeNode(x)
        i = inorder.index(x)
        # preorder.pop(0) ，此时preorder只剩 左右，:i是左部分
        node.left = self.buildTree2(preorder[:i], inorder[:i])
        node.right = self.buildTree2(preorder[i:], inorder[i + 1:])
        return node

