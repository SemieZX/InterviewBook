
## 先左边 记下lh 再右边 记下rh 最后比绝对值

def isBalance(head):
    if not head:
        return True
    res = [True]
    getHeight(head,1,res)
    return res[0]

def getHeight(head,level,res):
    if head == None:
        return level
    lh = getHeight(head.left, level+1, res)
    if res[0] == False:
        return level
    rh = getHeight(head.right, level+1, res)
    if res[0] == False:
        return level
    if abs(lh-rh) > 1:
        res[0] = False
    return max(lh,rh)