# 当stack中为空时，help元素从小到大排列，因此倒回stack中时，元素从大到小排列

def sortStackByStack(stack):
    help = []
    while len(stack) != 0:
        cur = stack.pop()
        while len(help) != 0 and cur > help[-1]:
            stack.append(help.pop())
        help.append(cur)
    while len(help) != 0:
        stack.append(help.pop())
    return stack
stack = [4,3,2,5]
print(sortStackByStack(stack))
