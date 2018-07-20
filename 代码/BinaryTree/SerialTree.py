# preOrder method

def serialByPre(root):
    if not root:
        return '#!'
    res = root.val + '!'
    res += serialByPre(root.left)
    res += serialByPre(root.right)
    return res

def reconBypreString(preStr):
    def reconPreOrder(values):
        value = values.pop(0)
        if value == '#':
            return None
        root = TreeNode(value)
        root.left = reconPreOrder(values)
        root.right = reconPreOrder(values)
        return root
    values = preStr.split('!')
    return reconBypreString(values)

# by Level

def serialByLevel(root):
    if root == '#':
        return '#!'
    queue = [ ]
    queue.append(root)
    res = root.val + '!'
    while queue:
        root = queue.pop(0)
        if root.left:
            res += root.left.val + '!'
            queue.append(root.left)
        else:
            res += '#!'
        
        if root.right:
            res += root.right.val + '!'
            queue.append(root.right)
        else:
            res += '#!'
    return res


def reconByLevelString(levStr):
    def generateNode(key):
        if key == '#':
            return None
        return TreeNode(key)
    values = levStr.split('!')
    head = generateNode(values.pop(0))
    queue = []
    if head:
        queue.append(head)
    while queue:
        root = queue.pop(0)
        root.left = generateNode(values.pop(0))
        root.right = generateNode(values.pop(0))
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
    return head
    


