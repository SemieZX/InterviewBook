
# soluion1  需要一个额外的栈结构

def isPalindrome(head):
    if head == None or head.next == None:
        return True
    stack = []
    cur = head
    while cur != None:
        stack.append(cur)
        cur = cur.next
    while stack:
        if stack.pop().val != head.val:
            return False
        head = head.next
    return True

# solution2 
def isPalindrome2(head):
    if head == None or head.next == None:
        return True
    stack = [ ]
    pre = head
    cur = head
    while cur.next != None and cur.next.next != None:
        pre = pre.next
        cur = cur.next.next
    pre = pre.next
    while pre != None:
        stack.append(pre)
        pre = pre.next
    while stack:
        if stack.pop().val != head.val:
            return False
        head = head.next
    return True

# solution3  

def isPalindrome3(head):
    if head == None or head.next == None:
        return True
    pre = head
    cur = head
    while cur.next != None and cur.next.next != None:
        pre = pre.next
        cur = cur.next.next
    # 用简单例子思考这里的点分别是什么
    nodefirst = pre.next
    pre.next = None
    while nodefirst != None:
        next = nodefirst.next
        nodefirst.next = pre
        pre = nodefirst
        nodefirst = next
    # 翻转完成
    
    node = pre #第二部分翻转后的头,记下
    res  = True
    while pre != None and head != None:
        if pre.val != head.val:
            res = False
            break
        pre = pre.next
        head = head.next
    pre = node.next
    node.next = None
    while pre != None:
        next = pre.next
        pre.next = node
        node = pre
        pre = next
    return res

