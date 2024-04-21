from collections import deque

def tree_by_levels(node):
    if node is None:
        return []

    queue = deque()
    queue.append(node)
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.value)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return result
