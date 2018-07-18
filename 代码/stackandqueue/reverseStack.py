#看书好好思考这个过程
def reverse(stack):
    if len(stack) == 0:
        return 
    i = getAndRemoveLastElemnet(stack)
    reverse(stack)
    stack.append(i)

def getAndRemoveLastElemnet(stack):
    res = stack.pop()
    if len(stack) == 0:
        return res
    else:
        last = getAndRemoveLastElemnet(stack)
        stack.push(res)
        return last 
