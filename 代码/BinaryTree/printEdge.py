
class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

# definition 1
def printRdge1(root):
    def getHeight(root,height=0):
        if not root:
            return height
        return max(getHight(root.left,height + 1), getHeight(root.right, height +1))

    def getMap(root, i ,map):
        if not root:
            return
        if map[i][0] == None:
            map[i][0] = root
        map[i][1] = root
        getmap(root.left, i+1, map)
        getmap(root.right, i+1,map)
    
    def printLeafNotInMap(root,i,map):
        if not root:
            return
        if not root.left and not root.right and root != map[i][0] and \
               root != map[i][1]:
            print(root.val, end = '')
        printLeafNotInMap(root.left, i+1, map)
        printLeafNotInMap(root.right,i+1, map)
    
    if not root:
        return
    height = getHeight(root)
    map = [[None for i in range(2)] for j in range(height)]
    getMap(root,0,map)
    # 打左边界
    for i in range(len(map)): #depth
        print(map[i][0].val , end = '')
    printLeafNotInMap(root,0,map) #打非左非右叶节点
    for i in range(len(map)-1,-1,-1):
        if map[i][0] != map[i][1]:
            print(map[i][1].val, end = '')


# definition2
def printEdge2(root):

    def printleft(root,isPrint):
        if not root:
            return 
        if isPrint or (root.left == None and root.right == None):
            print(root.val, end = '')
        printleft(root.left, isPrint)
        #打印右节点的情况，首先父节点必须isprint，其次其左节点必须为None
        printleft(root.right, isPrint and root.left == None)
    def printRight(root,isPrint):
        if not root:
            return
        printRight(root.left, isPrint and root.Right == None)
        printRight(root.right,isPrint)
        if isPrint or (root.left == None and root.right == None):
            print(root.val, end = '')

    if not root:
        return 
    print(root.val  , end = '')
    if root.left and root.right:
        printleft(root.left,True)
        printRight(root.left,True)
    #后两种属规模小的完整情况
    elif root.left:
        printEdge2(root.left)
    elif root.right:
        printEdge2(root.right)