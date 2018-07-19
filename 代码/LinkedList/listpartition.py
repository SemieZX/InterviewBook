# 链表 partition

def listPartition(head, pivot):
    def partition(nodeArr,pivot):
        left = -1
        right = len(nodeArr)
        index = 0
        #[0..left][left+1..index)[right..len(nodeArr)-1]
        while index < right:
            if nodeArr[index].val < pivot:
                left += 1
                nodeArr[left] , nodeArr[index] = nodeArr[index], nodeArr[left] 
                index += 1
            elif nodeArr[index].val == pivot:
                index += 1
            else:
                right -= 1
                nodeArr[index],nodeArr[right] = nodeArr[right], nodeArr[index]
    if head == None or head.next == None:
        return head
    
    cur = head
    n = 0 #链表长度
    while cur != None:
        n += 1
        cur = cur.next
    
    nodeArr = []
    cur = head
    while cur != None:
        nodeArr.append(cur)
        cur = cur.next
    partition(nodeArr,pivot)
    for i in range(n-1):
        nodeArr[i].next = nodeArr[i+1]
    nodeArr[-1].next = None #处理最后一个节点
    return nodeArr[0]



    # 进阶题目：按照原始节点对应顺序将链表分为三部分，之后将其连接起来

    def listPartition2(head, pivot):
        if head == None or head.next == None:
            return head
        sH = None # small head
        sT = None # small tail
        eH = None
        eT = None
        bH = None
        bT = None
        while head != None:
            next = head.next
            head.next = None
            if head.val < pivot:
                if sH == None:
                    sH = head
                    sT = head
                else:
                    sT.next = head
                    sT = head
            elif head.val == pivot:
                if eH == None:
                    eH = head
                    eT = head
                else:
                    eT.next =head
                    eT = head
            else:
                if bH == None:
                    bH = head
                    bT = head
                else:
                    bT.next = head
                    bT = head
            head = next #这一步很关键 采用很巧妙的方法遍历
        ## 这里考虑ST EH BH 
        if sT != None: # small connect equal
            head = sH
            if eH != None:
                sT.next = eH
            elif bH != None:
                sT.next = bH
        #这里考虑 eT head bH 
        if eT != None:
            head = head if head != None else eH
            if bH != None:
                eT.next = bH
        return head 
