from collections import deque

def topView(root):
    if not root:
        return root

    result = deque()
    head = root

    hasLeft = False
    
    if head.left:
        hasLeft = True
        while root:
            result.appendleft(root.data)
            root = root.left

    root = head
    if not hasLeft:
        result.append(root.data)
    if head.right:
        while root.right:
            result.append(root.right.data)
            root = root.right

    for element in result:
        print element, 
