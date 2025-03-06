class Node:
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right

def height(root):

    stack = [root]
    while stack:

        temp = [*stack]
        stack = []

        for node in temp:
            print(node.info, end=' ')
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

if __name__ == '__main__':
    root = Node(1, right=Node(2, right=Node(5, left=Node(3, right=Node(4)), right=Node(6))))