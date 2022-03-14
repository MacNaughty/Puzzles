"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def insert(r,val):
    if not r:
        new_node = Node(val)
        return new_node

    curr_node = r
    while curr_node:
        if val > curr_node.data:
            if curr_node.right:
                curr_node = curr_node.right
            else:
                curr_node.right = Node(val)
                break
        elif val < curr_node.data:
            if curr_node.left:
                curr_node = curr_node.left
            else:
                curr_node.left = Node(val)
                break

    return r
