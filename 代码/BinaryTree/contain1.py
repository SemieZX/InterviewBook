class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

#看t1是否包含t2
def contains(t1,t2):
    return check(t1,t2) or contains(t1.left,t2) or contains(t1.right,t2)

def check(h,t2):
    if t2 == None:
        return True
    if h == None or h.value != t2.value:
        return False
    return check(h.left,t2.left) and check(h.right, t2.right)
