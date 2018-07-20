
# Time O(N)

class Node:
    def __init__(self,val):
        self.val = val
        self.next = next
def removeRp1(head):
    if head == None or head.next == None:
        return head
    hashset = set()
    pre = head
    cur = head.next
    hashset.add(head.val)
    while cur != None:
        next = cur.next
        if cur.val not in hashset:
            hashset.add(cur.val)
            pre = cur
        else:
            pre.next = next # delete
        cur = next

# def 2

def removeRp2(head):
    if head == None or head.next == None:
        return head
    while head != None:
        pre = head
        cur = head.next
        while cur != None:
            if cur.val == head.val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        head = head.next