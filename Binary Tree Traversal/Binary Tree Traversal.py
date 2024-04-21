# Pre-order traversal
def pre_order(node):
    if node is None:
        return []

    stack = []
    result = []

    stack.append(node)

    while stack:
        node = stack.pop()
        result.append(node.data)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return result

# In-order traversal
def in_order(node):
    if node is None:
        return []

    stack = []
    result = []

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node.data)
            node = node.right

    return result

# Post-order traversal
def post_order(node):
    if node is None:
        return []

    stack = []
    result = []

    stack.append(node)

    while stack:
        node = stack.pop()
        result.insert(0, node.data)

        if node.left:
            stack.append(node.left)

        if node.right:
            stack.append(node.right)

    return result
