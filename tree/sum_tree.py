def toSumTree(root) :
    if root is None:
        return 0

    temp = root.data
    if root.left is None and root.right is None:
        root.data = 0

    root.data = toSumTree(root.left) + toSumTree(root.right)

    return root.data + temp