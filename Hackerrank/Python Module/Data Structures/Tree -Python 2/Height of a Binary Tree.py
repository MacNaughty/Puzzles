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


def check_node(root):
    left_sum = 0
    right_sum = 0

    if root.left:
        left_sum += 1 + check_node(root.left)

    if root.right:
        right_sum += 1 + check_node(root.right)

    if left_sum > right_sum:
        return left_sum
    else:
        return right_sum


def height(root):
    result = -1

    if root.info:
        result += 1
        left_sum = 0
        if root.left:
            left_sum = 1 + check_node(root.left)
        right_sum = 0
        if root.right:
            right_sum = 1 + check_node(root.right)

        if left_sum > right_sum:
            result += left_sum
        else:
            result += right_sum

    return result



tree = BinarySearchTree()
t = int(input())

for _ in range(t):
    x = int(input())
    tree.create(x)

print(height(tree.root))
