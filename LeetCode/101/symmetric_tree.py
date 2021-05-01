def isMirror(left: TreeNode, right: TreeNode):
    if not left and not right:
        return True
    elif left and right and left.val == right.val:
        return isMirror(left.left, right.right) and isMirror(left.right, right.left)
    else:
        return False


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return isMirror(root.left, root.right)
