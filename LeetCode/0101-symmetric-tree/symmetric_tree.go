func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	} else {
		return areNodesSymmetric(root.Left, root.Right)
	}
}

func areNodesSymmetric(left *TreeNode, right *TreeNode) bool {
	if left == nil && right == nil {
		return true
    } else if left == nil || right == nil {
        return false
    } else {
        return left.Val == right.Val && areNodesSymmetric(left.Left, right.Right) && areNodesSymmetric(left.Right, right.Left)
    }
}
