
def printInOrder(root, height,preStrs,length):
    if not root:
        return 
    printInOrder(root.right, height+1,'v',length)
    string = preStrs + root.val + preStrs
    leftLen = (length - len(string)) // 2
    rightlen = length - len(string) - leftLen
    res = " " *leftLen + string + " "*rightlen
    print(" "*height*length + res)
    printInOrder(root.left, height +1 , '^', length)

def printTree(root):
    if not root:
        return
    print('Binary Tree:  ')
    printInOrder(root,0,'H',17)

