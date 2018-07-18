# 单链表
def reverseList(head):
    if head == None:
        return 
    pre = None
    while head != None:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre

# 双链表

def reverseDoubleList(head):
    if head == None:
        return 
    pre = None
    while head != None:
        next = head.next
        head.next = pre
        head.pre = next
        pre = head
        head = next
    return pre
