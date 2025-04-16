from collections import deque

def level_order(root):
    if not root:
        return []

    queue = deque([root])          # Queue for BFS
    result = []                    # Final list of values

    while queue:
        node = queue.popleft()     # Pop from front of queue
        result.append(node.val)    # Visit current node

        if node.left:
            queue.append(node.left)   # Add left child if exists
        if node.right:
            queue.append(node.right)  # Add right child if exists

    return result