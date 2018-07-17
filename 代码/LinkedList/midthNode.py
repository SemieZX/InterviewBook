
# the mid
import math
def removeMidNode(head):

    if head == None or head.next == None:
        return head
    if head.next.next == None:
        return head.next
    
    pre = head
    cur = head.next.next
    #初始要删除的节点为 head.next 即pre.next
    while cur.next != None and cur.next.next != None:
        pre = pre.next
        cur = cur.next.next
    pre.next = pre.next.next
    return head

# the a/b th
def removeByRatio(head,a,b):

    if head == None or a < 1 or a > b:
        return head
    n = 0
    cur = head
    while cur != None: #算长度
        cur = cur.next
        n += 1
    n = math.ceil(a * n / b)
    if n == 1:
        return head.next
    cur = head
    while n-1 != 1: # 求前一个节点
        cur = cur.next
        n -= 1
    cur.next = cur.next.next
    return head
