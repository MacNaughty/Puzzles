def preOrder(root):
    #Write your code here
    print root.data, 
    if root.left:
        preOrder(root.left)
    if root.right:
        preOrder(root.right)
