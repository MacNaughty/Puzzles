def get_children(list_of_nodes, result):
    next_list_of_nodes = []
    for node in list_of_nodes:
        if node.left:
            result.append(node.left.data)
            next_list_of_nodes.append(node.left)
        if node.right:
            result.append(node.right.data)
            next_list_of_nodes.append(node.right)

    if len(next_list_of_nodes) > 0:
        get_children(next_list_of_nodes, result)



def levelOrder(root):
    if not root:
        return root

    list_of_nodes = []
    result = []
    list_of_nodes.append(root)
    result.append(root.data)
    get_children(list_of_nodes, result)

    for node_info in result:
        print node_info, 
