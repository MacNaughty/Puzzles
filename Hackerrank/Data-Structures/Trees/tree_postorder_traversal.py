from collections import deque


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def preOrder(root):
    stack = [root]
    d = deque()
    while stack:
        node = stack.pop()
        d.appendleft(node.info)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    print(*d)

if __name__ == '__main__':
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(5)
    root.right.right.left = Node(3)
    root.right.right.left.right = Node(4)
    root.right.right.right = Node(6)
    preOrder(root)