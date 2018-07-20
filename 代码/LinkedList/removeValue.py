
# method 1
def removeValue1(head,num):
    if head == None:
        return None
    stack = []
    while head != None:
        if head.val != num:
            stack.append(head)
        head = head.next

    while stack:
        stack[-1].next = head
        head = stack.pop()
    return head

# method 2
def removeValue2(head,num):
    if head == None:
        return head
    while head != None and head.val == num:
        head = head.next
    # 找到第一个不是num的节点
    pre = head
    cur = head
    while cur != None:
        if cur.val == num:
            pre.next = cur.next
        else:
            pre = cur
        cur = cur.next
    return head
    
