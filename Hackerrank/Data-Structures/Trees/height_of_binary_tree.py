class Node:
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right

def height(root):
    if not (root.left or root.right):
        return 0

    stack = [root]
    level = -1
    while stack:
        level += 1
        temp = []
        while stack:
            temp.append(stack.pop())

        for node in temp:
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
    return level


if __name__ == '__main__':
    root = Node(3, left=Node(2, left=Node(1)), right=Node(5, left=Node(4), right=Node(6, right=Node(7))))
    print(height(root))