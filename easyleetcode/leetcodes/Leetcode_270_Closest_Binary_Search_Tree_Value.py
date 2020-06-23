

class Solution(object):

    def closestValue(self, root, target):
        # compare kids' result with root
        kid = root.left if target < root.val else root.right
        if not kid:
            return root.val
        kid_min = self.closestValue(kid, target)
        return min((kid_min, root.val), key=lambda x: abs(target - x))

