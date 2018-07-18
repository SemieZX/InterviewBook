class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
def create_tree(root):
    element = input("Enter a key : ")
    if element == ' #':
        return None
    else:
        root = TreeNode(element)
        root.left = create_tree(root.left)
        root.right = create_tree(root.right)
    return root

## 前序
def pre_order(root):
    if root:
        print(root.val, end='')
        pre_order(root.left)
        pre_order(root.right)


def pre_order1(root):
    if not root:
        return 
    stack = []
    while root or len(stack):
        if root: #不断把从根到叶左子树设为root
            stack.append(root)
            print(root.val,end ='')
            root = root.left
        else:
            root = stack.pop()
            root = root.right   

## 中序

def mid_order(root):
    if root:
        mid_order(root.left)
        print(root.val, end = '')
        mid_order(root.right)

def mid_order1(root):
    if not root:
        return 
    stack =  []
    while root or stack:
        if root:
            stack.append(root) #先一直放，不输出
            root = root.left
        else:
            root = stack.pop()
            print(root.val, end = '')
            root = root.right

## 后序

def pos_order(root):
    if root:
        pos_order(root.left)
        pos_order(root.right)
        print(root.val, end = '')


def pos_order1(root):
    if not root:
        return
    stack1 = []
    stack2 = []
    while root or stack1:
        if root:
            stack1.append(root)
            stack2.append(root.val)
            root = root.right
        else:
            root = stack1.pop()
            root = root.left
    while stack2:
        print(stack2.pop(),end = '')


def pos_order2(root):
    if not root:
        return
    stack = []
    stack.append(root)
    c = None
    while stack:
        c = stack[-1]
        if c.left and c.left != root and c.right == root:
            stack.append(c.left)
        elif c.right and c.right != root:
            stack.append(c.right)
        else:
            print(stack.pop().val, end ='')
            root = c

#效率不高
def pos_order3(root):
    res = [ ]
    stack = [ ]
    p = root
    while stack or p :
        if p :
            stack.append(p)
           # reverse the preocess of preordertraversal
            res.insert(0,p.val)
            p = p.right
        else:
            node = stack.pop()
            p = node.left
    return res


