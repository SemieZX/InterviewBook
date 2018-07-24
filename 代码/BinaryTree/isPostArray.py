#判断数组是不是搜索二叉树的后序遍历结果

def isPostArray(arr):
    if arr == None or len(arr) == 0:
        return False
    return isPost(arr,0,len(arr)-1)
def isPost(arr,start,end):
    if start == end:
        return True
    less = -1
    more = end
    for i in range(start,end):
        if arr[i] < arr[end]:
            less = i
        else:
            more = i if more == end else more
    #一边没有的情况
    if less == -1 or more == end:
        return isPost(arr,start,end-1)
    #前边for循环使得less和more差1
    if less != more - 1:
        return False
    return isPost(arr,start,less) and isPost(arr,more,end-1)


# 通过arr 重构二叉树

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val 

def posArrayToBST(posArr):
    if posArr == None:
        return None
    return posToBST(posArr, 0, len(posArr)-1)

def posToBST(posArr, start, end):
    if start > end:
        return True
    head = Node(posArr[end])
    less = -1
    more = end
   for i in range(start,end):
        if posArr[i] < posArr[end]:
            less = i
        else:
            more = i if more == end else more
    head.left = posToBST(posArr,start,less)
    head.right = posToBST(posArr,more,end-1)
    return head


          