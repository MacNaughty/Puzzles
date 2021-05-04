class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res

        q = []
        stack = []
        q.append(root)

        while q:
            level = []

            for i in range(len(q)):
                node = q.pop(0)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                level.append(node.val)

            stack.append(level)

        while stack:
            res.append(stack.pop())

        return res
