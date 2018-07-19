
# Solution1 hashtable

class RandNode:
    def __init__(self,data):
        self.val = data
        self.next = None
        self.rand = None

def copyListWithRand1(head):
    if head == None:
        return None
    map = {}
    cur = head
    while cur != None:
        map[cur] = RandNode(cur.val)
        cur = cur.next
    cur = head
    while cur != None:
        map[cur].next = None if cur.next == None else map[cur.next]
        map[cur].rand = None if cur.rand == None else map[cur.rand]
        cur = cur.next 
    return map[head]




# Solution2
def copyListWithRand2(head):
    if head == None:
        return None
    # copy make  1-1-2-2-3-3
    cur = head
    while cur != None:
        next = cur.next
        cur.next  = RandNode(cur.val)
        cur.next.next = next
        cur =next 
    
    # setting rand
    cur = head
    while cur != None:
        cur.next.rand = None if cur.rand == None else cur.rand.next
        cur = cur.next.next
    
    copyHead = head.next # 1'
    cur = head
    while cur != None:
        next = cur.next
        cur.next = next.next
        next.next = None if cur.next == None else cur.next.next
        cur = cur.next
    return copyHead

