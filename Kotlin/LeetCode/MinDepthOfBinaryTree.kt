// Problem number 111

fun minDepth(root: TreeNode?): Int {
    if (root == null) return 0

    var result = 0
    val deque = ArrayDeque<TreeNode>().apply {
        add(root)
    }

    while (deque.isNotEmpty()) {
        result++
        for (i in 0 until deque.size) {
            var isLeaf = true
            val node = deque.removeFirst()

            node.left?.let {
                isLeaf = false
                deque.add(it)
            }

            node.right?.let {
                isLeaf = false
                deque.add(it)
            }

            if (isLeaf) {
                return result
            }
        }
    }
    return -1
}
