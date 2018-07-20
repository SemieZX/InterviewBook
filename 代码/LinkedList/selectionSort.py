
def selectionSort(head):
    def getSmallestPre(head):
        if head == None:
            return None
        pre = head
        smallest = head
        smallpre = None
        head = head.next
        while head != None:
            if head.val < smallest.val:
                smallest = head
                smallpre = pre
            pre = head
            head = head.next
        return smallpre
    if head == None or head.next == None:
        return head
    
    tail = None #排序部分的尾巴
    newHead = None #
    cur = head #未排序的头
    small = None #最小节点
    while cur != None:
        smallpre = getSmallestPre(cur) #最小节点前一个节点
        if smallpre != None:
            small = smallpre.next
            smallpre.next = small.next
        else:
            small = cur
            cur = cur.next
        #最小串里还没添加东西时
        if tail == None:
            tail = small
            newHead = tail
        else:
            tail.next = small
            tail = small
    return newHead

