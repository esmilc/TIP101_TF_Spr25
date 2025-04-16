def min_diff_in_bst(root):
    prev = [None]
    min_diff = [float('inf')]

    def in_order(node):
        if not node:
            return
        in_order(node.left)
        if prev[0] is not None:
            min_diff[0] = min(min_diff[0], node.val - prev[0])
        prev[0] = node.val
        in_order(node.right)

    in_order(root)
    return min_diff[0]